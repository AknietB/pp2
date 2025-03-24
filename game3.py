import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((800,800))
background_color=(255,255,255)
radius=25
color=(255,0,0)
position = [400,400]
speed=20
running=True
while running:
    screen.fill(background_color)
    pygame.draw.circle(screen,color,position,radius)
    pygame.display.update()
   
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP and position[1] - radius > 0:
                position[1] -= speed 
            if event.key == pygame.K_DOWN and position[1] + radius < 800:
                position[1] += speed 
            if event.key == pygame.K_LEFT and position[0] - radius > 0:
                position[0] -= speed 
            if event.key == pygame.K_RIGHT and position[0] + radius < 800:
                position[0] += speed 
pygame.quit()