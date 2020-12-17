import pygame
import os
import math
import random

# Setting up the display
pygame.init()
WIDTH, HEIGHT = 800,500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game!")
FPS = 60
clock = pygame.time.Clock()



# Button Variables
RADIUS = 18
GAP = 20
letters = []
startx = round((WIDTH-(RADIUS * 2 + GAP)*13)/2)
starty = 400
for i in range(26):
    x = startx + GAP  + (RADIUS * 2 + GAP) * (i%13)
    y = starty + ((i//13)*(GAP + RADIUS*2))
    letters.append([x, y, chr(65 + i), True])
# print(letters)


#fonts
TITLE_FONT = pygame.font.SysFont('comicsans',70)
LETTER_FONT = pygame.font.SysFont('comicsans',35)
WORD_FONT = pygame.font.SysFont('comicsans',45)



# Loading the images
images = []
background_image = pygame.image.load(".\images\\background.png")
redo_image = pygame.image.load(".\images\\redo.png")
for i in range(7):
    image = pygame.image.load(".\images\hangman" + str(i) + ".png")
    images.append(image)



# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (213, 227, 219)

# Setting up the game loop

def draw(word, guessed, hangman_status):
    win.blit(background_image,(0,0))
    # win.fill(WHITE)

    # Drawing the Title
    text = TITLE_FONT.render("HANGMAN", 1, GREY)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 30))

    # Drawing the no of lives left
    text = LETTER_FONT.render("Lives Left: " + str(6-hangman_status), 1, GREY)
    win.blit(text, (5,5))


    # Drawing Answer Words
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + "    "
        else:
            display_word += "_    "

    text = WORD_FONT.render(display_word, 1, GREY)
    win.blit(text, (370, 250))


    # Drawing Buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            # pygame.draw.circle(win, BLACK, (x,y), RADIUS, 2)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))

    # Display Everything
    win.blit(images[hangman_status],(150,100))
    pygame.display.update()


def drawBufferScreen(message):
    win.blit(background_image,(0,0))
    win.blit(images[6],(100,100))

    # Add BufferScreen Text
    text = TITLE_FONT.render(message, 1, GREY)
    win.blit (text, (WIDTH/2 - text.get_width()/2, HEIGHT/3 - text.get_height()/2))
    text = WORD_FONT.render("Would You like to play again?", 1, BLACK)
    win.blit (text, (WIDTH/2 - text.get_width()/2, 2*HEIGHT/3 - text.get_height()/2))

    # Add Redo Image
    win.blit(redo_image,(WIDTH/2-20,2*HEIGHT/3 - text.get_height()/2 + 50))

    # Display everything
    pygame.time.delay(500)
    pygame.display.update()

    # Returning the center coordinates of image
    return (WIDTH/2, 2*HEIGHT/3 - text.get_height()/2 + 70)



def mainScreen():
    # Game Variables
    hangman_status = 0
    words = ["DEVELOPER", "PYTHON", "PYGAME", "DEAD", "COMPUTER", "ANDROID"]
    word = random.choice(words)
    guessed = [" "]

    # Making all the letters Visible again
    for letter in letters:
        letter[3] = True

    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y , ltr, visible = letter
                    dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                    if dis<RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
        draw(word, guessed, hangman_status)

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            print
            BufferScreen("You Won!")
            break

        if hangman_status == 6:
            BufferScreen("You Lost!")
            break


def BufferScreen(message):
    run = True
    while run:
        clock.tick(FPS)

        x_center, y_center = drawBufferScreen(message)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                if abs(m_x-x_center)<=20 and abs(m_y-y_center)<=20:
                    run = False
                    print("Cicked on Redo Button!")
                    mainScreen()

mainScreen()


pygame.quit()
