import pygame

# ====================
# SETUP ==============
pygame.init()   #initializes pygame
gameDisplay = pygame.display.set_mode((800,600))    # define game's display or 'surface'
pygame.display.set_caption('A Bit Racey')   # set caption for window

clock = pygame.time.Clock() # define gameclock


# ====================
# GAME LOGIC =========
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print event

    pygame.display.update() #display.flip() will update entire surface
    clock.tick(60)  # wait for equivalent of 60fps

pygame.quit()
quit()

