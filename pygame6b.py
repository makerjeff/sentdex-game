## PYGAME2

import pygame
import time
import random

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

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

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

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    car_speed = 0
    car_width = 73

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
            ####### CONTROL LOGIC ########
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -50
                elif event.key == pygame.K_RIGHT:
                    x_change = 50
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            ##############################

            ### update position before telling where to draw the car ###
            x += x_change

            # print event
        gameDisplay.fill(white)

        #draw things
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        #draw car
        car(x, y)

        # WALL BOUNDARY LOGIC
        if x > display_width - car_width or x < 0:
            crash()

        # move 'thing' back to zero once it passes
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)

        # collision detection
        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()  # display.flip() will update entire surface
        clock.tick(60)  # wait for equivalent of 60fps



game_loop()
pygame.quit()
quit()

