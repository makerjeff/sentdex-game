## PYGAME2

import pygame
import time

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
car_img = pygame.image.load('racecar.png')

def car(x, y):
    gameDisplay.blit(car_img, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))   #center
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    gameExit = False
    x_change = 0
    car_speed = 0
    car_width = 73

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            ####### CONTROL LOGIC ########
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            ##############################

            # TODO: new logic
            # if key is pressed down
            # and if key is LEFT



            ### update position before telling where to draw the car ###
            x += x_change

            # print event
        gameDisplay.fill(white)
        car(x, y)

        # WALL BOUNDARY LOGIC
        if x > display_width - car_width or x < 0:
            crash()

        pygame.display.update()  # display.flip() will update entire surface
        clock.tick(60)  # wait for equivalent of 60fps



game_loop()
pygame.quit()
quit()

