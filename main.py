import random
import math
import pygame
from pygame import mixer

# intializing pygame
pygame.init()
# creating screen
screen = pygame.display.set_mode((800, 600))
# caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
# background music
pygame.mixer.music.load('background.wav')
mixer.music.play(-4)


def explosionmusic():
    sound = mixer.Sound("explosion.wav")
    sound.play()


# BACKGROUND IMAGE
backgorund = pygame.image.load('5438748.jpg')

# bullet image
bullet = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bullet_state = "ready"
bulletX_change = 0
bulletY_change = 4
# player
playerimg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
# score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
#credit
font2 = pygame.font.Font("freesansbold.ttf", 12)
creditX=698
creditY=575
textX = 10
textY = 10


def text(x, y):
    score = font.render("score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def credit(x,y):
    score = font2.render("made by abhiraj", True, (255, 255, 255))
    screen.blit(score, (x, y))





def game_over():
    over = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (200, 250))


# gameover font size
over_font = pygame.font.Font('freesansbold.ttf', 64)


# spaceship
def player(x, y):
    screen.blit(playerimg, (playerX, playerY))


# game over
def isgameover(playerX, playerY, enemyX, enemyY):
    dis = math.sqrt(math.pow(playerX - enemyX, 2) + math.pow(playerY - enemyY, 2))
    if dis < 40:
        return True


# collison

def iscollision(bulletX, bulletY, enemyX, enemyY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))

    if distance < 21:
        explosionmusic()

        return True
    # if enemyY>=480:
    #     enemyY[] = 2000
    #     over = over_font.render("GAME OVER", True, (255, 255, 255))
    #     screen.blit(over, (200, 250))


# def over(playerX,playerY,enemyX,enemyY):
#     distance=math.sqrt(math.pow(playerX-bulletX,2)+math.pow(playerY-bulletY,2))
#     if distance<27:
#         True


# enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for num in range(num_of_enemies):
    enemyimg.append(pygame.image.load('ghost.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.34)
    enemyY_change.append(40)


# enemyX=370
# enemyY=98
# bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 13, y + 10))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


# gameloop
run = True
while run:

    screen.blit(backgorund, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.4
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # get the current x coordinate of bullet
                    bulletX = playerX
                    sound = mixer.Sound("laser.wav")
                    sound.play()

                    fire_bullet(playerX, 480)
            # if event.key==pygame.K_UP:
            #     playerY_change=-0.3
            # if event.key==pygame.K_DOWN:
            #     playerY_change=+0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    for i in range(num_of_enemies):
        mm = isgameover(playerX, playerY, enemyX[i], enemyY[i])
        if mm or enemyY[i] > 500:
            for j in range(num_of_enemies):
                game_over()

                enemyY[j] = 2000

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX[i] = 0
            enemyY[i] += 40
            enemyX_change[i] = 0.34
        elif enemyX[i] >= 736:
            enemyX[i] = 736
            enemyY[i] += 40
            enemyX_change[i] = -0.34
        collison = iscollision(bulletX, bulletY, enemyX[i], enemyY[i])
        if collison:
            score_value += 1
            bulletY = 480
            bullet_state = "ready"
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    if playerY >= 536:
        playerY = 536

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)

        bulletY -= 0.83
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    player(playerX, playerY)

    text(textX, textY)
    credit(creditX,creditY)
    pygame.display.update()
