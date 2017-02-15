import pygame

pygame.init()   # initialize pygame

colors = {
    'white'   :(255,255,255),
    'black'   :(0,0,0),
    'red'     :(255,0,0),
    'green'   :(0,255,0),
    'blue'    :(0,0,255)
}

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(colors['black'])

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = colors['green']
