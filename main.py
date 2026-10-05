#Juego Tetris - Main
import pygame

pygame.init()
#1. Hacer la ventana del juego

ventana = pygame.display.set_mode((800, 600)) #ancho, alto
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ventana.fill((0, 0, 0)) #Color de fondo negro
    pygame.display.flip()
    clock.tick(60) #FPS

pygame.quit()
