import pygame

class Actions(pygame.sprite.Sprite):
    def __init__(self, posx: int, posy: int, speed: float, fps: int, surface: pygame.surface.Surface, scale: float = 1):
        super().__init__()
        self.scale = scale
        i = ["sprites/player/player_0.png", "sprites/player/player_1.png", "sprites/player/player_2.png"]
        self.frames = [pygame.transform.scale_by(pygame.image.load(j).convert_alpha(), self.scale) for j in i]
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
        self.backgroud_img = ""
        self.background_on = False
        self.python = pygame.transform.scale_by(pygame.image.load("sprites/python/python_normal.png"), 0.7)
        self.python_rect = self.python.get_rect(center = (-500, -500))
        self.pythonboss = pygame.transform.scale_by(pygame.image.load("sprites/python/python_boss.png"), 0.7)
        self.pythonboss_rect = self.pythonboss.get_rect(center = (-500, -500))
        self.java = pygame.image.load("sprites/java.png")
        self.java_rect = self.java.get_rect(center = (-500, -500))
        self.atk1 = pygame.transform.scale_by(pygame.image.load("sprites/atks/atk1.png"), 0.5)
        self.atk1_rect = self.atk1.get_rect(center = (-500, -500))
        self.atk2 = pygame.transform.scale_by(pygame.image.load("sprites/atks/atk2.png"), 0.5)
        self.atk2_rect = self.atk1.get_rect(center = (-500, -500))
        
        self.heart_frames = ["sprites/heart/heart_1.png", "sprites/heart/heart_2.png", "sprites/heart/heart_3.png", "sprites/heart/heart_4.png"
                             "sprites/heart/heart_5.png", "sprites/heart/heart_6.png" "sprites/heart/heart_7.png"]
        self.heart_fps = 4
        self.heart_index = 0
        self.heart = pygame.transform.scale_by(pygame.image.load(self.heart_frames[self.heart_index]), 0.5)
        self.heart_rect = self.heart.get_rect(center = (-500, -500))
        self.timewait = 0
    
    def process_tasks(self):
        if self.actions_to_do:
            task, *args = self.actions_to_do[0]
            done = task(*args)
            if done:
                self.actions_to_do.pop(0)
                self.runningx = 0
                self.runningy = 0
    
    # Funções do protagonista
    def goto(self, rect, tox: int, toy: int):
        self.actions_to_do.append((self.goto_process, rect, tox, toy))

    def goto_process(self, rect, tox: int, toy:int):
        dx = rect.centerx - tox
        dy = rect.centery - toy
        move = False
        
        if dx > 0:
            rect.centerx -= self.speed
            dx = rect.centerx - tox
            if dx < 0:
                rect.centerx = tox
            move = True
        
        if dx < 0:
            rect.centerx += self.speed
            dx = rect.centerx - tox
            if dx > 0:
                rect.centerx = tox
            move = True
                
        if dy > 0:
            rect.centery -= self.speed
            dy = rect.centery - toy
            if dy < 0:
                rect.centery = toy
            move = True
        
        if dy < 0:
            rect.centery += self.speed
            dy = rect.centery - toy
            if dy > 0:
                rect.centery = toy
            move = True
                    
        if dx == 0 and dy == 0:
            move = False
        
        if rect == self.rect:
            self.walking = move
        return not move
    
    def runto(self, rect, runx: int, runy:int):
        self.actions_to_do.append((self.runto_process, rect, runx, runy))
        
    def runto_process(self, rect, runx: int, runy: int):
        moverun = False
        
        if self.runningx < runx:
            self.runningx += self.speed
            rect.centerx += self.speed
            if self.runningx > runx:
                rect.centerx -= self.runningx - runx
                self.runningx = runx
            moverun = True
        
        if self.runningx > runx:
            self.runningx -= self.speed
            rect.centerx -= self.speed
            if self.runningx < runx:
                rect.centerx += self.runningx - runx
                self.runningx = runx
            moverun = True
                
        if self.runningy < runy:
            self.runningy += self.speed
            rect.centery += self.speed
            if self.runningy > runy:
                rect.centery -= self.runningy - runy
                self.runningy = runy
            moverun = True
        
        if self.runningy > runy:
            self.runningy -= self.speed
            rect.centery -= self.speed
            if self.runningy < runy:
                rect.centery += self.runningy - runy
                self.runningy = runy
            moverun = True
            
        if rect == self.rect:
            self.walking = moverun
        return not moverun
    
    def teleport(self, rect, posx: int, posy:int):
        self.actions_to_do.append((self.teleport_process, rect, posx, posy))
    
    def teleport_process(self, rect, posx: int, posy: int):
       rect.centerx = posx
       rect.centery = posy
       return True
    
    def ballon(self, speech: str, speed_speech: float = 0.1, time: float = 5):
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
        
    def background(self, image: str):
        self.actions_to_do.append((self.background_process, image))
    
    def background_process(self, image: str):
        self.backgroud_img = pygame.image.load(image)
        self.background_on = True
        return True
    
    def background_show(self):
        if self.background_on:
            self.surface.blit(self.backgroud_img, (0,0))
    
    def show_sprites(self):
        self.surface.blit(self.python, self.python_rect)
        self.surface.blit(self.java, self.java_rect)
        self.surface.blit(self.heart, self.heart_rect)
        self.surface.blit(self.pythonboss, self.pythonboss_rect)
        self.surface.blit(self.atk1, self.atk1_rect)
        self.surface.blit(self.atk2, self.atk2_rect)
    
    def wait(self, time: int):
        self.actions_to_do.append((self.wait_process, time))
    def wait(self, time: int):
        if self.timewait > time*60:
            self.timewait += 1
            return False
        else:
            self.timewait = 0
            return True
    def animation(self):
        if self.walking:
            self.index += (1/60) * self.fps
            self.image = self.frames[int(self.index % len(self.frames))]
        else:
            self.index = 0
            self.image = self.frames[self.index]
    
    def update(self):
        self.process_tasks()
        self.background_show()
        self.show_sprites()
        self.ballon_show()
        self.animation()
