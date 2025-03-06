import pygame
from sys import exit
import core_animation
import os

pygame.init()
w_w = 800
w_h = 400
icon = pygame.image.load("sprites/python/python_normal.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Anifinal - LuSiThi")
screen = pygame.display.set_mode((w_w, w_h))
clock = pygame.time.Clock()
background = pygame.image.load("sprites/background/background1.png")
pythonzinho = core_animation.Actions(["sprites/player/player_0.png", "sprites/player/player_1.png", "sprites/player/player_2.png"], 100, 170, 2, 12, screen, 0.5)

pythonzinho_group = pygame.sprite.GroupSingle()
pythonzinho_group.add(pythonzinho)
def cena1():
    pythonzinho.ballon("Olá, esse é um dialógo massa!", 0.1, 5)
    pythonzinho.runto(300, 20)
    for _ in range(7):
        pythonzinho.runto(-20, 0)
        pythonzinho.runto(20, 0)
    pythonzinho.ballon("Jurandy Games", 0.1, 10)
    
    
cena1()
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0,0))
    pythonzinho_group.draw(screen)
    pythonzinho_group.update()
            
    pygame.display.update()
    clock.tick(60)