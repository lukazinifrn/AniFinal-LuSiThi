import pygame
from sys import exit
from random import randint
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
    animation.ballon("JOSEFINO: Onde eu estou?", 0.3, 4)
    animation.ballon("JOSEFINO: Olá? Tem alguém aqui?", 0.3, 4)
    animation.runto(animation.rect,400,50)
    animation.ballon("JOSEFINO: Oh, que flores lindas!")
    animation.runto(animation.rect,0,-50)
    
def cena2():
    animation.teleport(animation.rect, -500, -500)
    animation.background("./sprites/background/background2.png")
    animation.teleport(animation.python_rect, w_w/2, w_h/2)
    animation.ballon("JOSEFINO: Ué, mas o que é isso no meio das flores?", 0.3, 5)
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
    animation.ballon("""PYTHON: print("Prepare-se para as consequências!!!")""", 0.5, 3)
    animation.ballon("""PYTHON: print("Você atrapalhou minha compilação!!!")""", 0.5, 4)
    animation.ballon("""PYTHON: print("SEU SEM AMOR PATERNO!!!!!!!!!!!")""", 0.5, 4)
    
def cena3():
    animation.teleport(animation.rect, -500, -500)
    animation.background("./sprites/background/background3.png")
    animation.teleport(animation.pythonboss_rect, w_w/2, 70)
    animation.teleport(animation.heart_rect, w_w/2-10, w_h/2+30)
    animation.play_music(0.5)
    animation.ballon("""PYTHON: print("Boa sorte em desviar disso HAHHAHHAHAH")""", 0.4, 5)
    animation.goto(animation.heart_rect, 300, 240)
    animation.teleport(animation.atk1_rect, w_w/2-10, w_h/2+30)
    animation.goto(animation.heart_rect, 450, 250)
    animation.teleport(animation.atk1_rect, 300, 200)
    animation.goto(animation.heart_rect, 450, 310)
    animation.teleport(animation.atk1_rect, 450, 250)
    animation.goto(animation.heart_rect, 330, 310)
    animation.teleport(animation.atk1_rect, 450, 290)
    animation.goto(animation.heart_rect, 330, 180)
    animation.teleport(animation.atk1_rect, 330, 310)
    animation.teleport(animation.atk1_rect, -500, -500)
    animation.teleport(animation.heart_rect, w_w/2-10, w_h/2+30)
    animation.ballon("""PYTHON: print("Como...")""", 0.4, 2)
    animation.ballon("""PYTHON: print("COMO VOCÊ DESVIOU DOS MEUS ATAQUES?")""", 0.4, 5)
    animation.ballon("JOSEFINO: Bem...", 0.08, 4)
    animation.ballon("JOSEFINO: Foi bem, fácil.", 0.2, 4)
    animation.ballon("JOSEFINO: Você é lento.", 0.2, 4)
    animation.ballon("""PYTHON: print("Você realmente disse o que eu ouvi???")""", 0.6, 4)
    animation.ballon("""PYTHON: print("Maldito.")""", 0.6, 1)
    animation.ballon("""PYTHON: print("Maldito!")""", 0.6, 1)
    animation.ballon("""PYTHON: print("MALDITO!!!")""", 0.6, 1)
    animation.ballon("""PYTHON: print("Vamos ver quem é lento...")""", 0.1, 7)
    animation.teleport(animation.atk2_rect, w_w/2-10, w_h/2-20)
    animation.goto(animation.heart_rect, w_w/2-90, w_h/2+30)
    animation.goto(animation.atk2_rect, w_w/2-10, w_h/2+30)
    animation.goto(animation.heart_rect, w_w/2-90, w_h/2-20)
    animation.goto(animation.atk2_rect, w_w/2-45, w_h/2+20)
    animation.goto(animation.atk2_rect, w_w/2-70, w_h/2)
    animation.goto(animation.heart_rect, w_w/2+70, w_h/2-20)
    animation.goto(animation.atk2_rect, w_w/2-60, w_h/2-20)
    animation.goto(animation.atk2_rect, w_w/2+70, w_h/2-20)
    animation.ballon("""PYTHON: print("HAHA! Quem é o lento agora?")""", 0.3, 4)
    animation.ballon("""PYTHON: print("MORRA!!!")""", 0.5, 3)
    animation.teleport(animation.atk1_rect, -500, -500)
    animation.teleport(animation.heart_rect, w_w/2-10, w_h/2+30)
    animation.stop_music()
    
def cena4():
    animation.background("sprites/background/background4.png")
    animation.teleport(animation.atk1_rect, -500, -500)
    animation.teleport(animation.heart_rect, -500, -500)
    animation.teleport(animation.atk2_rect, -500, -500)
    animation.teleport(animation.pythonboss_rect, -500, -500)
    animation.teleport(animation.rect, -500, -500)
    animation.wait(3)
    animation.ballon("JOSEFINO: Ah...", 0.15, 2)
    animation.ballon("JOSEFINO: É assim que tudo vai acabar?", 0.2, 3)
    animation.ballon("JOSEFINO: Eu morri para um Python...?", 0.25, 4)
    animation.ballon("JOSEFINO: Minha morte foi tão rídicula como minha vida...", 0.3, 4)
    animation.ballon("JOSEFINO: Parando para pensar...", 0.3, 4)
    animation.ballon("JOSEFINO: Um inútil como eu teve um destino digno, de fato.", 0.3, 4)
    animation.wait(3)

def cena5():
    animation.background("sprites/background/background5.png")
    animation.teleport(animation.rect, 200, w_h/2)
    animation.ballon("JOSEFINO: Hã? Que lugar estranho é esse?", 0.2, 4)
    animation.runto(animation.java_rect, -500, 0)
    animation.ballon("JOSEFINO: Espera...", 0.1, 4)
    animation.runto(animation.rect, 100, 0)
    animation.ballon("JOSEFINO: UM JAVA?????", 0.4, 3)
    animation.ballon("""JAVA: System.out.println("Acertou!!");""", 0.3, 3)
    animation.ballon("""JAVA: System.out.println("Está feliz em me ver, né?");""", 0.4, 4)
    animation.ballon("JOSEFINO: Na verdade, não. Estou com medo.", 0.5, 3)
    animation.ballon("""JAVA: System.out.println("Ah...");""", 0.4, 4)
    animation.ballon("""JAVA: System.out.println("Relaxa...");""", 0.4, 4)
    animation.ballon("""JAVA: System.out.println("Eu vi que você está tendo problemas.");""", 0.5, 4)
    animation.ballon("""JAVA: System.out.println("É com o Python né?.");""", 0.5, 4)
    animation.ballon("JOSEFINO: Sim... acho que ele quase me matou.", 0.5, 3)
    animation.ballon("""JAVA: System.out.println("Bem, eu vou te ajudar!");""", 0.5, 4)
    animation.goto(animation.javapower_rect, w_w/2, w_h/2-20)
    animation.ballon("""JAVA: System.out.println("Vou te dar um pouco do poder do Java.");""", 0.5, 4)
    animation.ballon("""JAVA: System.out.println("Isso te deixará mais rápido!");""", 0.5, 4)
    animation.ballon("JOSEFINO: Caraca Javão... muito obrigado.", 0.4, 4)
    animation.ballon("""JAVA: System.out.println("De nada... Boa sorte.");""", 0.5, 4)
    animation.ballon("JOSEFINO: Tamo junto, parceiro.", 0.4, 5)
    animation.background("sprites/background/background4.png")
    animation.wait(3)

def cena6():
    animation.teleport(animation.rect, -500, -500)
    animation.teleport(animation.java_rect, -500, -500)
    animation.teleport(animation.javapower_rect, -500, -500)
    animation.background("sprites/background/background3.png")
    animation.teleport(animation.pythonboss_rect, w_w/2, 70)
    animation.teleport(animation.heart_rect, w_w/2-10, w_h/2+30)
    animation.play_music(0.5)
    animation.ballon("""PYTHON: print("Mas o quê???")""", 0.5, 3)
    animation.ballon("""PYTHON: print("Como você não morreu?")""", 0.5, 4)
    animation.ballon("JOSEFINO: Bem, isso não te interessa.", 0.4, 5)
    animation.ballon("JOSEFINO: Cai para briga logo.", 0.4, 5)
    for _ in range(180):
        animation.teleport(animation.heart_rect, randint(250, 500), randint(170, 300))
    animation.ballon("""PYTHON: print("QUÊ?")""", 0.5, 2)
    animation.ballon("""PYTHON: print("Você está muito rápido!")""", 0.5, 4)
    animation.ballon("""PYTHON: print("Como eu vou acertar você? Não é justo!")""", 0.5, 4)
    animation.ballon("JOSEFINO: Faz o L, amigo.", 0.4, 4)
    animation.ballon("JOSEFINO: Você perdeu!", 0.5, 3)
    animation.goto(animation.atk_player_rect, w_w/2-10, 70)
    animation.ballon("""PYTHON: print(AHHHHHHH)""", 0.5, 4)
    animation.ballon("ERROR: name 'AHHHHHHH' is not defined", 0.7, 4)
    animation.ballon("Fatal error", 0.7, 2)
    animation.teleport(animation.atk_player_rect, -500, -500)
    animation.teleport(animation.pythonboss_rect, -500, -500)
    animation.teleport(animation.heart_rect, -500, -500)
    animation.teleport(animation.python_rect, w_w/2-10, 70)
    animation.ballon("JOSEFINO: Parece que eu venci o Python...", 0.4, 4)
    animation.stop_music()

def cena7():
    animation.teleport(animation.python_rect, -500, -500)
    animation.background("./sprites/background/background1.png")
    animation.teleport(animation.rect, w_w/2+ 65, w_h/2 )
    animation.ballon("JOSEFINO: Ah... finalmente uma paz...", 0.15, 6)
    animation.ballon("JOSEFINO: Espero não ter que enfrentar...", 0.3, 4)
    animation.ballon("JOSEFINO: Outra linguagem de programação...", 0.3, 4)
    animation.goto(animation.c_rect, 700, w_h/2)
    animation.ballon("""std::cout << "Hey! Eu sou o C++";""", 0.5, 4)
    animation.ballon("""std::cout << "Sua briguinha com o Python...";""", 0.5, 4)
    animation.ballon("""std::cout << "Atrapalhou 0.000001 segundos da minha compilação!";""", 0.6, 4)
    animation.ballon("""std::cout << "Prepare-se!!!!!!!!!!";""", 0.4, 3)
    animation.ballon("JOSEFINO: Ah, mas nem funde-", 0.4, 1)

def cena8():
    animation.teleport(animation.c_rect, -500, -500)
    animation.teleport(animation.rect, -500, -500)
    animation.background("sprites/background/background6.png")
    animation.teleport(animation.playernormal_rect, 150, 230)
    animation.ballon("JOSEFINO: AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH", 0.6, 4)
    animation.ballon("JOSEFINO: Quê?", 0.3, 3)
    animation.ballon("JOSEFINO: Foi tudo um sonho?", 0.4, 3)
    animation.ballon("...", 0.05, 5)
    animation.ballon("JOSEFINO: Parece que não foi uma boa ideia ficar programando...", 0.5, 5)
    animation.ballon("JOSEFINO: E jogando Undertale até tarde.", 0.5, 4)
    animation.ballon("JOSEFINO: Que sonho louco...", 0.5, 3)
    animation.ballon("JOSEFINO: Vou ficar longe do computador por um tempo...", 0.7, 3)
    animation.runto(animation.playernormal_rect, 0, 50)
    animation.runto(animation.playernormal_rect, 900, 0)
    
def cena9():
    animation.background("sprites/background/background4.png")
    animation.teleport(animation.rect, -500, -500)
    animation.teleport(animation.c_rect, -200, w_h/2)
    animation.play_music(0.7)
    animation.ballon("FIM...", 0.1, 5)
    animation.ballon("A lição do dia é: Programem em Java!", 0.3, 5)
    animation.goto(animation.c_rect, w_w/2, w_h/2)
    animation.ballon("""std::cout << "NÃAAAAOOO,  programem em C++!!";""", 0.5, 4)
    animation.goto(animation.bone_rect, w_w/2, w_h/2)
    for k in range(90):
        l = k * 5
        animation.teleport(animation.c_rect, w_w/2 - l,  w_h/2 - l/2)
        animation.teleport(animation.bone_rect, -500, -500)
    animation.teleport(animation.bone_rect, -500, -500)
    animation.goto(animation.sans_rect, w_w/2, w_h/2)
    animation.ballon("SANS: Negativo. A lição do dia é: não programem.", 0.4, 5)
    animation.runto(animation.sans_rect, -700, 0)
    animation.ballon("Agora sim...FIM...", 0.1, 10)
    animation.stop_music()
    
cena = int(input(menu))

if cena == 1:
    cena1()
    cena2()
    cena3()
    cena4()
    cena5()
    cena6()
    cena7()
    cena8()
    cena9()

elif cena == 2:
    cena2()
    cena3()
    cena4()
    cena5()
    cena6()
    cena7()
    cena8()
    cena9()
    
elif cena == 3:
    cena3()
    cena4()
    cena5()
    cena6()
    cena7()
    cena8()
    cena9()
    
elif cena == 4:
    cena4()
    cena5()
    cena6()
    cena7()
    cena8()
    cena9()
    
elif cena == 5:
    cena5()
    cena6()
    cena7()
    cena8()
    cena9()

elif cena == 6:
    cena6()
    cena7()
    cena8()
    cena9()

elif cena == 7:
    cena7()
    cena8()
    cena9()

elif cena == 8:
    cena8()
    cena9()

elif cena == 9:
    cena9()

elif cena == 10:
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