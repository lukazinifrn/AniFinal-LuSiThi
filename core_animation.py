import pygame

class Actions(pygame.sprite.Sprite):
    def __init__(self, frames: list, posx: int, posy: int, speed: float, fps: int, surface, scale: float = 1):
        super().__init__()
        self.scale = scale
        self.frames = [pygame.transform.scale_by(pygame.image.load(i).convert_alpha(), self.scale) for i in frames]
        self.fps = fps
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(center=(posx, posy))
        self.speed = speed
        self.walking = False
        self.runningx = 0
        self.runningy = 0
        self.ballonsurface = pygame.image.load("sprites/ballon.png")
        self.ballonrect = self.ballonsurface.get_rect(topleft = (0, 272))
        self.font = pygame.font.Font("fonts/DTM-Mono.otf", 20)
        self.ballonindex = 0
        self.ballontime = 0
        self.ballon_on = False
        self.surface = surface
        self.ballonword = ""
        self.actions_to_do = []
        
    def add_task(self, task, *args):
        self.actions_to_do.append((task, args))
        
    def process_tasks(self):
        if self.actions_to_do:
            task, *args = self.actions_to_do[0]
            done = task(*args)
            if done:
                self.actions_to_do.pop(0)
                self.runningx = 0
                self.runningy = 0
                
    def goto(self, tox: int, toy: int):
        self.actions_to_do.append((self.goto_process, tox, toy))

    def goto_process(self, tox: int, toy:int):
        dx = self.rect.centerx - tox
        dy = self.rect.centery - toy
        move = False
        
        if dx > 0:
            self.rect.centerx -= self.speed
            dx = self.rect.centerx - tox
            if dx < 0:
                self.rect.centerx = tox
            move = True
        
        if dx < 0:
            self.rect.centerx += self.speed
            dx = self.rect.centerx - tox
            if dx > 0:
                self.rect.centerx = tox
            move = True
                
        if dy > 0:
            self.rect.centery -= self.speed
            dy = self.rect.centery - toy
            if dy < 0:
                self.rect.centery = toy
            move = True
        
        if dy < 0:
            self.rect.centery += self.speed
            dy = self.rect.centery - toy
            if dy > 0:
                self.rect.centery = toy
            move = True
                    
        if dx == 0 and dy == 0:
            move = False
            
        self.walking = move
        return not move
    
    def runto(self, runx: int, runy:int):
        self.actions_to_do.append((self.runto_process, runx, runy))
        
    def runto_process(self, runx: int, runy: int):
        moverun = False
        
        if self.runningx < runx:
            self.runningx += self.speed
            self.rect.centerx += self.speed
            if self.runningx > runx:
                self.rect.centerx -= self.runningx - runx
                self.runningx = runx
            moverun = True
        
        if self.runningx > runx:
            self.runningx -= self.speed
            self.rect.centerx -= self.speed
            if self.runningx < runx:
                self.rect.centerx += self.runningx - runx
                self.runningx = runx
            moverun = True
                
        if self.runningy < runy:
            self.runningy += self.speed
            self.rect.centery += self.speed
            if self.runningy > runy:
                self.rect.centery -= self.runningy - runy
                self.runningy = runy
            moverun = True
        
        if self.runningy > runy:
            self.runningy -= self.speed
            self.rect.centery -= self.speed
            if self.runningy < runy:
                self.rect.centery += self.runningy - runy
                self.runningy = runy
            moverun = True
        
        self.walking = moverun
        return not moverun
    
    def teleport(self, posx: int, posy:int):
        self.actions_to_do.append((self.teleport_process, posx, posy))
    
    def teleport_process(self, posx: int, posy: int):
        self.rect.centerx = posx
        self.rect.centery = posy
        return True
    
    def ballon(self, speech: str, speed_speech: float, time: float):
        self.actions_to_do.append((self.ballon_process, speech, speed_speech, time))
    
    def ballon_process(self, speech: str, speed_speech: float, time: float):
        if not(self.ballon_on):
            pygame.mixer.Sound("audio/ballon.mp3").play()
        if len(self.ballonword) != len(speech):
            self.ballonindex += speed_speech
            self.ballonword = speech[0: int(self.ballonindex)]
            self.ballon_on = True
        else:
            if self.ballontime < 60*time:
                self.ballontime += 1
            else:
                self.ballon_on = False
                self.ballonword = ""
                self.ballontime = 0
                self.ballonindex = 0
                return True
                        
    def ballon_show(self):
        if self.ballon_on:
            text = self.font.render(self.ballonword, False, "white")
            textrect = text.get_rect(topleft = (self.ballonrect.left + 16, self.ballonrect.top + 16))
            self.surface.blit(self.ballonsurface, self.ballonrect)
            self.surface.blit(text, textrect)
        
    def animation(self):
        if self.walking:
            self.index += (1/60) * self.fps
            self.image = self.frames[int(self.index % len(self.frames))]
        else:
            self.index = 0
            self.image = self.frames[self.index]
    
    def update(self):
        self.process_tasks()
        self.ballon_show()
        self.animation()
