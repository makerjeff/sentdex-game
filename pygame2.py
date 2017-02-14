## PYGAME2

import pygame

# ====================
# SETUP ==============
pygame.init()   #initializes pygame

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))    # define game's display or 'surface'
pygame.display.set_caption('A Bit Racey')   # set caption for window

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock() # define gameclock


# ====================
# GAME LOGIC =========
crashed = False
car_img = pygame.image.load('racecar.png')

def car(x, y):
    gameDisplay.blit(car_img, (x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        # print event
    gameDisplay.fill(white)
    car(x,y)

    pygame.display.update() #display.flip() will update entire surface
    clock.tick(60)  # wait for equivalent of 60fps

pygame.quit()
quit()

