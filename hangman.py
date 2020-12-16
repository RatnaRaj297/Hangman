import pygame
import os

# Setting up the display
pygame.init()
WIDTH, HEIGHT = 800,500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game!")


# Loading the images
images = []
background_image = pygame.image.load(".\images\\background.png")
for i in range(7):
    image = pygame.image.load(".\images\hangman" + str(i) + ".png")
    images.append(image)


# Game Variables
hangman_status = 0


# Colors
WHITE = (255,255,255)


# Setting up the game loop
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)

    win.blit(background_image,(0,0))
    win.blit(images[hangman_status],(150,100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)


pygame.quit()
