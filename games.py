from tkinter import font
import pygame
import math
import random

#...初始化pygame
pygame.init()

#...Creat the screen
screen = pygame.display.set_mode((800, 600))

#...Background
background = pygame.image.load('pic/bg.jpg')

#...Title And Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('pic/ufo.png')
pygame.display.set_icon(icon)

#...Player
playerImg = pygame.image.load('pic/player.png')
playerX = 370
playerY = 480
playerX_change = 0

#...Enemt
enemyImg = pygame.image.load('pic/enemy.png')
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 0.5
enemyY_change = 40

#...Ready - You can't see the bullet on the screen
#...Fire - The bullet is currently moving
#...Bullet
bulletImg = pygame.image.load('pic/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = 'ready'

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
    
def show_text(text, x, y):#專門顯示文字的方法，除了顯示文字還能指定顯示的位置
    x = x
    y = y
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (x, y))
font = pygame.font.SysFont('arial', 34)
score_f = pygame.font.SysFont('arial', 34)

#...Main Game Loop
running = True
while running:
    #...set screen RGB
    screen.fill((0, 0, 0))
    #...Background Image
    screen.blit(background, (0, 0)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #...if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    #...Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    #...Checking for boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    #...Enemy Movement
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.5
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.5
        enemyY += enemyY_change
    #...Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    #...Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        score += 1
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)
    text = "Score: "
    score_text = str(score)
    show_text(text, 30, 0)
    show_text(score_text, 130, 0)
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()