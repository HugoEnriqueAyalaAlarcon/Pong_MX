import pygame, sys
pygame.init()

ALTO_VENTANA=600
ANCHO_VENTANA=900
ventana=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Galeria img")

def imagen():
    imagen_a_mostrar=pygame.image.load("img/pngegg_0.png")
    ventana.blit(imagen_a_mostrar,[0,0])#cagar imagen en ventana

def imagen_1(): # dimencionando la img a la ventana
    ancho_deseado = (ANCHO_VENTANA*.80)
    alto_deseado = (ALTO_VENTANA*.95)

    imagen_a_mostrar=pygame.image.load("img/pngegg_0.png")
    imagen_redimensionada = pygame.transform.scale(imagen_a_mostrar, (ancho_deseado, alto_deseado))
    medidas_img=imagen_redimensionada.get_rect()

    print(medidas_img)

    ancho_img=medidas_img[2]
    alto_img=medidas_img[3]
    ventana.blit(imagen_redimensionada,[(ANCHO_VENTANA//2)-(ancho_img//2),(ALTO_VENTANA//2)-(alto_img//2)])#cagar imagen en ventana

def imagen_2(numero_img): # dimencionando la img a la ventana
    ruta_img="img/pngegg_"+str(numero_img)+".png"
    print(ruta_img)
    ancho_deseado = (ANCHO_VENTANA*.70)
    alto_deseado = (ALTO_VENTANA*.95)
    imagen_a_mostrar=pygame.image.load(ruta_img)
    imagen_redimensionada = pygame.transform.scale(imagen_a_mostrar, (ancho_deseado, alto_deseado))
    medidas_img=imagen_redimensionada.get_rect()# medidas de la img
    #print(medidas_img)  
    ancho_img=medidas_img[2]
    alto_img=medidas_img[3]
    ventana.blit(imagen_redimensionada,[(ANCHO_VENTANA//2)-(ancho_img//2),(ALTO_VENTANA//2)-(alto_img//2)])#cagar imagen en ventana

num_img=0

while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT and num_img<9:
                num_img+=1  
            if event.key==pygame.K_LEFT and num_img>0:
                num_img-=1   

   
   #zona de dibujo           
    ventana.fill((255,255,255))
    #dibujar img
    imagen_2(num_img)
    pygame.display.flip()
