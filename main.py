import pygame
from sys import exit
import core_animation
from LuSiThi.menus import menu

pygame.init()
w_w = 800
w_h = 400
icon = pygame.image.load("sprites/python/python_normal.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Anifinal - LuSiThi")
screen = pygame.display.set_mode((w_w, w_h))
clock = pygame.time.Clock()


animation = core_animation.Actions(100, 170, 2, 12, screen, 0.5)


group = pygame.sprite.Group()
group.add(animation)


def cena1():
    animation.background("./sprites/background/background1.png")
    animation.teleport(animation.printatk_rect, 300, 200)
    animation.ballon("JOSEFINO: Onde eu estou?", 0.3, 4)
    animation.ballon("JOSEFINO: Olá? Tem alguém aqui?", 0.3, 4)
    animation.runto(animation.rect,400,50)
    animation.ballon("JOSEFINO: Oh, que flores lindas!")
    animation.runto(animation.rect,0,-50)
    
def cena2():
    animation.teleport(animation.rect, -500, -500)
    animation.background("./sprites/background/background2.png")
    animation.teleport(animation.python_rect, w_w/2, w_h/2)
    animation.ballon("JOSEFINO: Ué, mas o que é isso no meio dos flores?", 0.3, 5)
    for _ in range(90):
        if _%4 <= 2:
            animation.teleport(animation.pythonboss_rect, w_w/2, w_h/2)
            animation.teleport(animation.python_rect, -500, -500)
        else:
            animation.teleport(animation.python_rect, w_w/2, w_h/2)
            animation.teleport(animation.pythonboss_rect, -500, -500)
            
    animation.teleport(animation.pythonboss_rect, w_w/2, w_h/2)
    animation.teleport(animation.python_rect, -500, -500)
    animation.wait(2)
    animation.ballon("PYTHON: Prepare-se para as consequências!!!", 0.5, 3)
    animation.ballon("PYTHON: Você atrapalhou minha copilação!!!", 0.5, 4)
    animation.ballon("PYTHON: SEU SEM AMOR PATERNO!!!!!!!!!!!", 0.5, 4)
    
def cena3():
    animation.teleport(animation.rect, -500, -500)
    animation.background("./sprites/background/background3.png")
    animation.teleport(animation.pythonboss_rect, w_w/2, 70)
    animation.teleport(animation.heart_rect, w_w/2-10, w_h/2+30)
    animation.ballon("Boa sorte em desviar disso HAHHAHHAHAH", 0.4, 4)
    animation.runto(animation.heart_rect, 40, 0)
    animation.teleport(animation.atk1_rect, w_w/2-10, w_h/2+30)
    animation.runto(animation.heart_rect, -100, -20)
    animation.teleport(animation.atk1_rect, w_w/2-30, w_h/2+30)
    animation.runto(animation.heart_rect, +70, -20)
    animation.teleport(animation.atk1_rect, w_w/2+70, w_h/2-20)
    
    
def cena4():
    pass

cena = int(input(menu))

if cena == 1:
    cena1()
    cena2()
    cena3()
    cena4()

elif cena == 2:
    cena2()
    cena3()
    cena4()
elif cena == 3:
    cena3()
    cena4()
elif cena == 4:
    cena4()
elif cena == 5:
    pass

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()

    group.update()                 
    group.draw(screen)

            
    pygame.display.update()
    clock.tick(60)