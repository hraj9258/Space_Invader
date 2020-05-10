import pygame

# initlizing the pygame
pygame.init()

#creating the pygame screen
screen = pygame.display.set_mode((800, 600))

# starting the gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False