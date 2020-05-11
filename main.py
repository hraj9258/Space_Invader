import pygame

# initlizing the pygame
pygame.init()

#creating the pygame screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invader!")
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)

#player
playerImg = pygame.image.load("spaceship.png")
playerx=370
playery=480

def player():
    screen.blit(playerImg,(playerx,playery))

# starting the gameloop
running = True
while running:
    #RGB (red, green, blue)
    screen.fill((0, 125, 125))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()
