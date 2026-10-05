#Juego Tetris - Main
from tkinter import font

import pygame

pygame.init()

#Ventana del juego
ventana = pygame.display.set_mode((800, 600)) #ancho, alto
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

arial = pygame.font.SysFont("arial", 36)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ventana.fill((0, 0, 0)) # R, G, B - Color de fondo negro 0 0 0

    Titulo = arial.render("Tetris", True, (255, 255, 255))
    ventana.blit(Titulo, (480, 20))

    pygame.draw.rect(ventana, (255, 255, 255), (25, 25, 450, 550), 3) #x,y,ancho,alto,
    pygame.draw.line(ventana, (0, 255, 0), (485, 56), (550, 56), 2)

    pygame.display.flip() #Dibuja
    clock.tick(8) #FPS
pygame.quit()


