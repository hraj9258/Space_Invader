import pygame
import random

# initializing the pygame
pygame.init()

# creating the pygame screen
screen = pygame.display.set_mode((800, 600))  # 800 is width and 600 is height

# background
background = pygame.image.load("assets/background.png")

# Title and Icon
pygame.display.set_caption("Space Invader!")
logo = pygame.image.load("assets/logo.png")
pygame.display.set_icon(logo)

# player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load("assets/enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load("assets/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 25
bullet_state = "ready"

# score

score_value = 0
font = pygame.font.Font("Baby_Boomer.ttf", 32)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 125, 125))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))  # blit is used to show the image


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))  # blit is used to show the image


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    bulXenmX = (bulletX - enemyX)**2
    bulYenmY = (bulletY - enemyY)**2
    distance = (bulXenmX + bulYenmY)**0.5
    if distance < 27:
        return True
    else:
        return False


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
                    bulletX = playerX  # store the value of x where the space_bar has been pressed
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
    for i in range(num_of_enemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # collision
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:  # Checks if the bullet has crossed the limits
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":  # fires the bullet
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
