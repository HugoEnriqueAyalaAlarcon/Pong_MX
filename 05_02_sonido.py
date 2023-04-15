import pygame, sys
pygame.init()

ventana=pygame.display.set_mode((500,500))
pygame.display.set_caption("sonido")

musica=pygame.mixer.Sound("sound/musica.ogg")#cargar los archivos de auidio
punto=pygame.mixer.Sound("sound/punto.ogg")
golpe=pygame.mixer.Sound("sound/golpe.ogg")

while True: #ciclo principal del juego
    for event in pygame.event.get(): #rastrear eventos
        print(event)
        if event.type == pygame.QUIT: #si se preciona tache en la ventana
            sys.exit() #salir

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                musica.play(0)
                pygame.mixer.Sound.set_volume(musica,0.07)
            if event.key==pygame.K_s:
                punto.play(0)
                pygame.mixer.Sound.set_volume(punto,0.5)
            if event.key==pygame.K_d:
                golpe.play(0,800)
                pygame.mixer.Sound.set_volume(golpe,0.5)