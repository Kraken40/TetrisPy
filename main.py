#Juego Tetris - Main
import pygame

pygame.init()

#Ventana del juego
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA)) #ancho, alto
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

arial = pygame.font.SysFont("arial", 36)

#GUI
COLUMNAS = 10
FILAS = 18
TAMANO_CELDA = 30

ANCHO_TABLERO = COLUMNAS * TAMANO_CELDA
ALTO_TABLERO = FILAS * TAMANO_CELDA

ventana.fill((0, 0, 0)) # R, G, B - Color de fondo negro 0 0 0

def dibujar_tablero():
    pygame.draw.rect(ventana, (255, 255, 255), (25, 25, ANCHO_TABLERO, ALTO_TABLERO), 3)

    # Líneas verticales
    for columna in range(COLUMNAS + 1):
        x = 25 + columna * TAMANO_CELDA
        pygame.draw.line(ventana, (80, 80, 80), (x, 25), (x, 25 + ALTO_TABLERO))

    # Líneas horizontales
    for fila in range(FILAS + 1):
        y = 25 + fila * TAMANO_CELDA
        pygame.draw.line(ventana, (80, 80, 80), (25, y), (25 + ANCHO_TABLERO, y))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ventana.fill((0, 0, 0))

    dibujar_tablero()

    pygame.display.flip()
    clock.tick(60)


    ventana.fill((0, 0, 0))

    dibujar_tablero()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()