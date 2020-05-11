import pygame

# initlizing the pygame
pygame.init()

#creating the pygame screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invader!")
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)

# starting the gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #RGB (red, green, blue)
    screen.fill((0, 125, 125))
    pygame.display.update()
