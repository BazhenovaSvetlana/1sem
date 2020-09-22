import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 200), 100, 0)
circle(screen, (255, 0, 0), (160, 190), 20, 0)
circle(screen, (255, 0, 0), (240, 190), 13, 0)
circle(screen, (0, 0, 0), (160, 190),10, 0)
circle(screen, (0, 0, 0), (240, 190), 5, 0)
rect(screen, (0, 0, 0), (150, 250, 100, 20), 0)
polygon(screen, (0, 0, 0), [(90,130), (90,140), (190,180), (190,170)], 0)
polygon(screen, (0, 0, 0), [(220,170), (220,180), (270,170), (270,160)], 0)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
