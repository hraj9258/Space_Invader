import pygame
import random

# initializing the pygame
pygame.init()

# creating the pygame screen
screen = pygame.display.set_mode((800, 600))  # 800 is width and 600 is height

# background
background = pygame.image.load("background.png")

# Title and Icon
pygame.display.set_caption("Space Invader!")
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)

# player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 370)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 25
bullet_state = "ready"

def player(x, y):
    screen.blit(playerImg, (x, y))  # blit is used to show the image


def enemy(x, y):
    screen.blit(enemyImg, (x, y))  # blit is used to show the image


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# starting the gameloop
running = True
while running:
    # RGB (red, green, blue)
    screen.fill((0, 125, 125))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check weather it is for right or left
        if event.type == pygame.KEYDOWN:  # checks for key press
            if event.key == pygame.K_a:
                playerX_change = -5
            if event.key == pygame.K_d:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX # store the value of x where the space_bar has been pressed 
                    bullet_fire(bulletX, bulletY)

        if event.type == pygame.KEYUP:  # check for key release
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0  # stops the movement of player

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    # bullet movement
    if bulletY <= 0: # Checks if the bullet has crossed the limits  
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire": # fires the bullet
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
