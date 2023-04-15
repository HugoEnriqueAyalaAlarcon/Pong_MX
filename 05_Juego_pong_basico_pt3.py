#--------Juego Pon basico-------#
import pygame,sys
pygame.init()

#zona variables
ancho_ventana=(pygame.display.get_desktop_sizes()[0][0])
alto_ventana=(pygame.display.get_desktop_sizes()[0][1]*.85)

screen=pygame.display.set_mode(((ancho_ventana),(alto_ventana)))
pygame.display.set_caption("Pong basico") #titulo ventana

#colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
CAFE_C=(171,89,89)
AZUL_C=(200,221,238)
VERDE_C=(101,142,100)
AMARILLO_C=(236,218,158)

#cordenadas de la pelota
coord_pelota_x=(ancho_ventana//2)
coord_pelota_y=(alto_ventana//2)

speed_x=3
speed_y=3

#tamaño de la pelota
tam_pelota=8

#tamaño de barras
players_ancho=(ancho_ventana*.02)
players_alto=(ancho_ventana*.10)

#coorddenadas jugador 1
player_1_x_coord=10 # juegador 1 eje x se separa 10 px del lado izq de la ventana
player_1_y_coord=(alto_ventana//2) 
player_1_y_speed=0 # la velocidad  dependera de las tecla mas adelante lo veremos

#coorddenadas jugador 2
player_2_x_coord=(ancho_ventana-((ancho_ventana*.02)+10))
player_2_y_coord=(alto_ventana//2) 
player_2_y_speed=0 

#reloj
clock=pygame.time.Clock()

#sonidos
musica=pygame.mixer.Sound("sound/musica.ogg")
punto=pygame.mixer.Sound("sound/punto.ogg")
golpe=pygame.mixer.Sound("sound/golpe.ogg")

#funciones
def textos(fuente="arial",tam_txt=50,contenido="sin contenido",color=NEGRO,x=100,y=100):
    font=pygame.font.SysFont(fuente,tam_txt) 
    text=font.render(contenido,True,color)
    screen.blit(text,(x,y))
    medidas=text.get_rect()
    print(medidas)  

def menu():
    while True:
        for event in pygame.event.get(): #Rastrea eventos
            if event.type==pygame.QUIT:
                sys.exit()

            if event.type==pygame.KEYDOWN: #si tenemos un evento de precionar una tecla
                if event.key==pygame.K_SPACE: 
                    return True
                if event.key==pygame.K_ESCAPE: 
                    return False
     #zona dibujo
        textos("Chilanka",25,"Preciona Espacio:",CAFE_C,(ancho_ventana//2)-(201/2),(alto_ventana//2)+(42)) #texto preciona espacio
        textos("Chilanka",20,"continuar",CAFE_C,(ancho_ventana//2)-(74/2),(alto_ventana//2)+(90)) #texto preciona espacio
        textos("Chilanka",25,"Esc:",CAFE_C,(ancho_ventana//2)-(201/2),(alto_ventana//2)+(120)) #texto preciona espacio
        textos("Chilanka",20,"para salir",CAFE_C,(ancho_ventana//2)-(74/2),(alto_ventana//2)+(150))
        pygame.display.flip()
        clock.tick(60)

def inicio():
    saltar=False
    while saltar==False:
        for event in pygame.event.get(): #Rastrea eventos
            if event.type==pygame.QUIT:
                sys.exit()

            if event.type==pygame.KEYDOWN: #si tenemos un efento de precionar una tecla
                if event.key==pygame.K_SPACE: #si se preciona la tecla spac
                    saltar=True 
     #zona dibujo
        screen.fill(AZUL_C)
        textos("Ani",50,"PONG MX",NEGRO,(ancho_ventana//2)-(253//2),(alto_ventana//2)-(84//2))#texto pong
        textos("Ani",25,"Preciona Espacio",NEGRO,(ancho_ventana//2)-(183/2),(alto_ventana//2)+(84//2)) #texto preciona espacio
        pygame.display.flip()
        clock.tick(60)                

def juego(coord_pelota_x,coord_pelota_y,player_1_y_coord,player_2_y_coord,player_2_y_speed,player_1_y_speed,speed_x,speed_y):
    score_player_1=0
    score_player_2=0
    alto_fondo_score=30
    while True:
     # Zona de evento
        for event in pygame.event.get(): #Rastrea eventos
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN: #si tenemos un efento de precionar una tecla
                if event.key==pygame.K_ESCAPE: #si se preciona la tecla esc
                    pygame.mixer.Sound.stop(musica)
                    if (menu()==False):
                        return
                    pygame.mixer.Sound.play(musica,-1)
                    
                #jugador 1
                if event.key==pygame.K_w: #si la tecla que se preciono es w (se mueve hacia ariba el jugador 1)
                    player_1_y_speed=-3
                if event.key==pygame.K_s: #si la tecla que se preciono es s (se mueve hacia bajo el juagador 1)
                    player_1_y_speed=+3
                #jugador 2
                if event.key==pygame.K_UP: #si la tecla que se preciono es flecha ariba (se mueve hacia ariba el jugador 2)
                    player_2_y_speed=-3
                if event.key==pygame.K_DOWN: #si la tecla que se preciono es flecha abajo (se mueve hacia bajo el juagador 2)
                    player_2_y_speed=+3

            if event.type==pygame.KEYUP: #si hay un evento tipo KEYUP (si se libera una tecla)
                #jugador 1
                if event.key==pygame.K_w: #si la tecla que se libera es w (se mueve hacia ariba el jugador 1)
                    player_1_y_speed=0
                if event.key==pygame.K_s: #si la tecla que se libera es s (se mueve hacia bajo el juagador 1)
                    player_1_y_speed=0
                #jugador 2
                if event.key==pygame.K_UP: #si la tecla que se libera es flecha ariba (se mueve hacia ariba el jugador 2)
                    player_2_y_speed=0
                if event.key==pygame.K_DOWN: #si la tecla que se libera es  flecha abajo (se mueve hacia bajo el juagador 2)
                    player_2_y_speed=0
            
     # Zona logica
        # si la pelota sale por los costatos incrementar puntos
        if (coord_pelota_x < 0):
            punto.play(0,800)
            pygame.mixer.Sound.set_volume(punto,0.7)
            score_player_2+=1
            coord_pelota_x=(ancho_ventana//2)
            coord_pelota_y=(alto_ventana//2)
         

        if coord_pelota_x>(ancho_ventana):
            punto.play(0,800)
            pygame.mixer.Sound.set_volume(punto,0.5)
            score_player_1+=1
            coord_pelota_x=(ancho_ventana//2)
            coord_pelota_y=(alto_ventana//2)

        if (coord_pelota_y>((alto_ventana)-(tam_pelota+alto_fondo_score)) or coord_pelota_y < tam_pelota):
            speed_y*=-1

        #jugador 1 evitar que salga de ventana
        if player_1_y_coord>(alto_ventana-(players_alto+alto_fondo_score)) or player_1_y_coord <0:
            player_1_y_speed=0
            if player_1_y_coord >= (alto_ventana-(players_alto+alto_fondo_score)):
                player_1_y_coord = (alto_ventana-(players_alto+alto_fondo_score))
            if player_1_y_coord <= 0:
                player_1_y_coord = 0
        #jugador 2 evitar que salga de ventana
        if player_2_y_coord>(alto_ventana-(players_alto+alto_fondo_score)) or player_2_y_coord <0:
            player_2_y_speed=0
            if player_2_y_coord >= (alto_ventana-(players_alto+alto_fondo_score)):
                player_2_y_coord = (alto_ventana-(players_alto+alto_fondo_score))
            if player_2_y_coord <= 0:
                player_2_y_coord = 0

        #jugador 1 movimiento
        player_1_y_coord+=player_1_y_speed
        player_2_y_coord+=player_2_y_speed

        coord_pelota_x+=speed_x
        coord_pelota_y+=speed_y

     # Zona dibujo
        screen.fill(AZUL_C)
        pelota=pygame.draw.circle(screen,VERDE_C,(coord_pelota_x,coord_pelota_y),tam_pelota)
        player_1=pygame.draw.rect(screen,CAFE_C,(player_1_x_coord,player_1_y_coord,players_ancho,players_alto))
        player_2=pygame.draw.rect(screen,CAFE_C,(player_2_x_coord,player_2_y_coord,players_ancho,players_alto))
        fondo_escore=pygame.draw.rect(screen,BLANCO,(0,(alto_ventana-alto_fondo_score),ancho_ventana,alto_ventana))
        textos("Ani",50,"PONG MX",NEGRO,(ancho_ventana//2)-(253//2),(alto_ventana//2)-(84//2))
        textos("Ani",20,"Pts Jugador 1 = " + str(score_player_1),NEGRO,(ancho_ventana*.10),(alto_ventana)-(30))
        textos("Ani",20,"Pts Jugador 2 = " + str(score_player_2),NEGRO,(ancho_ventana*.75),(alto_ventana)-(30)) 
        pygame.display.flip()
        clock.tick(60)

     # Zona de coliciones
        #colicion de pelota con jugador
        if pelota.colliderect(player_1) or pelota.colliderect(player_2):
            golpe.play(0)
            pygame.mixer.Sound.set_volume(golpe,0.9)#bajar volumen
            speed_x*=-1

def fin():
    reiniciar=False
    while reiniciar==False:
        for event in pygame.event.get(): #Rastrea eventos
            if event.type==pygame.QUIT:
                sys.exit()

            if event.type==pygame.KEYDOWN: #si tenemos un efento de precionar una tecla
                if event.key==pygame.K_SPACE: 
                    reiniciar=True 
                if event.key==pygame.K_ESCAPE: 
                    sys.exit()
     #zona dibujo 
        pygame.draw.rect(screen, VERDE_C , (0,0,ancho_ventana,alto_ventana-30))
        textos("Ani",150,"PONG MX",NEGRO,(ancho_ventana//2)-(731//2),30)#texto pong
        textos("Ani",85,"Creditos: H. E. A. A.",NEGRO,(ancho_ventana//2)-(723//2),250) #texto preciona espacio
        textos("Ani",40,"Esc=Salir del juego, Espacio=reiniciar",NEGRO,(ancho_ventana//2)-(658/2),(alto_ventana//2)+(162//2)) #texto preciona espacio
        pygame.display.flip()
        clock.tick(60)                



while True:
    inicio()
    musica.play(-1)#play(-1) ciclar la musica infinitamente
    pygame.mixer.Sound.set_volume(musica,0.1)#bajar volumen
    juego(coord_pelota_x,coord_pelota_y,player_1_y_coord,player_2_y_coord,player_2_y_speed,player_1_y_speed,speed_x,speed_y)
    fin()
