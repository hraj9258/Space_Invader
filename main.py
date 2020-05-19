import pygame
from pygame import mixer
import random

# initializing the pygame
pygame.init()

# creating the pygame screen
screen = pygame.display.set_mode((800, 600))  # 800 is width and 600 is height

# background
background = pygame.image.load("assets/background.png")

# background music
backmusic = mixer.music.load("assets/background.wav")
mixer.music.set_volume(0.7)
mixer.music.play(-1)

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

# Accuracy
no_of_hit = 0

acur_text = 100
acur_font = pygame.font.Font("Baby_Boomer.ttf", 30)

acurX = 600
acurY = 10

# No of fire

num_of_fire = 0
num_fire_font = pygame.font.Font("freesansbold.ttf", 20)

numfX = 630
numfY = 80


# Game Over
gameover_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 125, 125))
    screen.blit(score, (x, y))


def show_acur(x, y):
    acur = acur_font.render("Accuracy: " + str(acur_text), True, (225, 225, 225))
    screen.blit(acur, (x, y))


def show_numfire(x, y):
    num_fire = num_fire_font.render("Bullet Fired:" + str(num_of_fire), True, (225, 225, 225, 0.1))
    screen.blit(num_fire, (x, y))


def game_over_text():
    game_over = gameover_font.render("GAME OVER", True, (225, 225, 225))
    screen.blit(game_over, (200, 250))


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
                    bullet_sound = mixer.Sound("assets/laser.wav")
                    bullet_sound.play()
                    num_of_fire += 1
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

        # game over
        if enemyY[i] > playerY:
            for j in range(num_of_enemy):
                enemyY[j] = 2000
            game_over_text()
            mixer.music.stop()
            break

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
            collision_sound = mixer.Sound("assets/explosion.wav")
            mixer.Sound.set_volume(collision_sound,0.7)
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            no_of_hit += 1
            if num_of_fire == 0:
                pass
            else:
                acur_text = (no_of_hit/num_of_fire)*100
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:  # Checks if the bullet has crossed the limits
        acur_text = (no_of_hit/num_of_fire)*100
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":  # fires the bullet
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    show_acur(acurX, acurY)
    show_numfire(numfX, numfY)
    pygame.display.update()
