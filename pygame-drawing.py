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

pygame.draw.line(gameDisplay, colors['blue'], (100,200), (300,400), 5)
pygame.draw.rect(gameDisplay, colors['red'], (400,400,50,25),5)
pygame.draw.circle(gameDisplay, colors['white'], (150,150), 75)
pygame.draw.polygon(gameDisplay, colors['green'], ((25,75),(76,125),(250,375),(400,25),(60,540)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()