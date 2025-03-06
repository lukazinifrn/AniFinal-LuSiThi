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

# Carrega os cenários
background1, background2, background3, background4 = pygame.image.load("sprites/background/background1.png"),pygame.image.load("sprites/background/background2.png"),pygame.image.load("sprites/background/background3.png"),pygame.image.load("sprites/background/background4.png")
# Para carregar o background
backgroundcena1, backgroundcena2, backgroundcena3, backgroundcena4 = False, False, False, False

protagonista = core_animation.Actions(["sprites/player/player_0.png", "sprites/player/player_1.png", "sprites/player/player_2.png"], 100, 170, 2, 12, screen, 0.5)
python_boss = core_animation.Actions(["sprites/python/python_normal.png"], 2000, 2000, 2, 12, screen, 0.7)
python = core_animation.Actions(["sprites/python/python_boss.png"], 2000, 2000, 2, 12, screen, 0.7)
coracao1 = core_animation.Actions(["sprites/python/python_boss.png"], -200, -200, 2, 12, screen, 0.7)
coracao2 = core_animation.Actions(["sprites/python/python_boss.png"], -200, -200, 2, 12, screen, 0.7)

group = pygame.sprite.Group()
group.add(protagonista)

group.add(python_boss)

def cena1():
    protagonista.background("./sprites/background/background1.png")
    protagonista.ballon("Josefino: Onde eu estou?",speed_speech=0.2,time=0.1)
    protagonista.ballon("Josefino: Ola? Tem alguem aqui?", time=0.1)
    protagonista.runto(400,50)
    protagonista.ballon("Josefino: Oh, que flores lindas!")
    protagonista.runto(0,-50)
    
    
def cena2():
    protagonista.background("./sprites/background/background2.png")
    protagonista.runto(200,200)
    python_boss.goto(w_w/2,w_h/2)
    python_boss.ballon("Josefino: O que é isso no meio das flores?", 0.2, 3)
    python_boss.ballon("Python: Prepare-se para a batalha!!", 0.15)

def cena3():
    protagonista.background("./sprites/background/background3.png")
    

def cena4():
    protagonista.background("./sprites/background/background4.png")

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