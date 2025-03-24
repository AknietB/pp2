import pygame
from datetime import datetime
pygame.init()
screen=pygame.display.set_mode((800,800))
clock=pygame.time.Clock()
first_image=pygame.image.load("labs/lab7/clock.png")
second_image=pygame.image.load("labs/lab7/min_hand.png")
third_image=pygame.image.load("labs/lab7/sec_hand.png")
rect=first_image.get_rect(center=(400,300))
running=True
while running:
    screen.blit(first_image,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        time=datetime.now().time()
        sec_angle=-time.second*6
        nsec_image=pygame.transform.rotate(second_image,sec_angle)
        sec_rect=nsec_image.get_rect(center=rect.center)
        screen.blit(nsec_image,sec_rect.topleft)

        min_angle=-time.minute*6
        nthird_image=pygame.transform.rotate(third_image,min_angle)
        min_rect=nthird_image.get_rect(center=rect.center)
        screen.blit(nthird_image,min_rect.topleft)
        pygame.display.flip()
        clock.tick(60)