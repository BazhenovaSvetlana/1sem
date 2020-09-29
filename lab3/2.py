import pygame
from pygame.draw import *
pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 560))

################################################################################
def draw_dom(x,y,k):
    polygon(screen, (255, 204, 0), [(x - 30*k, y - 40*k), (x + 40*k, y - 30*k), (x + 40*k, y + 40*k), (x - 30*k, y + 30*k)], 0)
    polygon(screen, (0, 0, 0), [(x - 30*k, y - 40*k), (x + 40*k, y - 30*k), (x + 40*k, y + 40*k), (x - 30*k, y + 30*k)], 1)
    polygon(screen, (255, 204, 0), [(x + 40*k, y - 30*k), (x + 70*k, y - 50*k), (x + 70*k, y + 20*k), (x + 40*k, y + 40*k)], 0)
    polygon(screen, (0, 0, 0), [(x + 40*k, y - 30*k), (x + 70*k, y - 50*k), (x + 70*k, y + 20*k), (x + 40*k, y + 40*k)], 1)
    polygon(screen, (255, 153, 0), [(x - 30*k, y - 40*k), (x + 10*k, y - 90*k), (x + 40*k, y - 30*k)], 0)
    polygon(screen, (0, 0, 0), [(x - 30*k, y - 40*k), (x + 10*k, y - 90*k), (x + 40*k, y - 30*k)], 1)
    polygon(screen, (255, 153, 0), [(x + 10*k, y - 90*k), (x + 40*k, y - 110*k), (x + 70*k, y - 50*k), (x + 40*k, y - 30*k)], 0)
    polygon(screen, (0, 0, 0), [(x + 10*k, y - 90*k), (x + 40*k, y - 110*k), (x + 70*k, y - 50*k), (x + 40*k, y - 30*k)], 1)
    circle(screen, (0, 0, 0), (x, y), 20*k, 0) 
################################################################################
def draw_zabor(x, y, k):
    for i in range(20):
        rect(screen, (255, 204, 102), (x+i*20*k, y, 20*k, 240*k), 0)
        rect(screen, (0, 0, 0), (x+i*20*k, y, 20*k, 240*k), 1)
################################################################################
def draw_sobaka(x, y, k, orientacia):

    if orientacia == True :
        ellipse(screen, (128, 128, 128), (x-70*k, y-40*k, 120*k, 50*k), 0)
        ellipse(screen, (128, 128, 128), (x-100*k, y-50*k, 60*k, 40*k), 0)
        ellipse(screen, (128, 128, 128), (x-110*k, y-30*k, 30*k, 30*k), 0)
        ellipse(screen, (128, 128, 128), (x-70*k, y-50*k, 30*k, 30*k), 0)
        ellipse(screen, (128, 128, 128), (x-110*k, y-10*k, 10*k, 50*k), 0) 
        ellipse(screen, (128, 128, 128), (x-70*k, y-30*k, 10*k, 50*k), 0)
        ellipse(screen, (128, 128, 128), (x-110*k, y+30*k, 30*k, 10*k), 0)
        ellipse(screen, (128, 128, 128), (x-70*k, y+10*k, 30*k, 10*k), 0)
        ellipse(screen, (128, 128, 128), (x+30*k, y-30*k, 30*k, 60*k), 0)
        ellipse(screen, (128, 128, 128), (x-10*k, y-10*k, 30*k, 60*k), 0)
        ellipse(screen, (128, 128, 128), (x+40*k, y+20*k, 30*k, 10*k), 0)
        ellipse(screen, (128, 128, 128), (x, y+40*k, 30*k, 10*k), 0)
        rect(screen, (128, 128, 128), (x, y-60*k, 50*k, 50*k), 0)
        rect(screen, (0, 0, 0), (x, y-60*k, 50*k, 50*k), 1)
        ellipse(screen, (255, 0, 0), (x+20*k, y-30*k, 10*k, 17*k), 0)
        ellipse(screen, (128, 128, 128), (x+10*k, y-50*k, 30*k, 30*k), 0)        
        ellipse(screen, (0, 0, 0), (x+10*k, y-50*k, 30*k, 30*k), 1)
        rect(screen, (128, 128, 128), (x+10*k, y-50*k, 30*k, 20*k), 0)
        ellipse(screen, (128, 128, 128), (x+40*k, y-60*k, 20*k, 20*k), 0)
        ellipse(screen, (0, 0, 0), (x+40*k, y-60*k, 20*k, 20*k), 1)
        ellipse(screen, (128, 128, 128), (x-10*k, y-60*k, 20*k, 20*k), 0)
        ellipse(screen, (0, 0, 0), (x-10*k, y-60*k, 20*k, 20*k), 1)    
        ellipse(screen, (255, 255, 255), (x+30*k, y-50*k, 10*k, 6*k), 0) 
        ellipse(screen, (0, 0, 0), (x+30*k, y-50*k, 10*k, 6*k), 1)
        ellipse(screen, (255, 255, 255), (x+10*k, y-50*k, 10*k, 6*k), 0)
        ellipse(screen, (0, 0, 0), (x+10*k, y-50*k, 10*k, 6*k), 1)
        ellipse(screen, (0, 0, 0), (x+13*k, y-50*k, 4*k, 6*k), 0)
        ellipse(screen, (0, 0, 0), (x+33*k, y-50*k, 4*k, 6*k), 0)
    
    elif orientacia == False :
        ellipse(screen, (128, 128, 128), (x-50*k, y-40*k, 120*k, 50*k), 0)
        ellipse(screen, (128, 128, 128), (x+40*k, y-50*k, 60*k, 40*k), 0)
        ellipse(screen, (128, 128, 128), (x+80*k, y-30*k, 30*k, 30*k), 0)
        ellipse(screen, (128, 128, 128), (x+40*k, y-50*k, 30*k, 30*k), 0)
        ellipse(screen, (128, 128, 128), (x+100*k, y-10*k, 10*k, 50*k), 0)
        ellipse(screen, (128, 128, 128), (x+60*k, y-30*k, 10*k, 50*k), 0)
        ellipse(screen, (128, 128, 128), (x+80*k, y+30*k, 30*k, 10*k), 0)
        ellipse(screen, (128, 128, 128), (x+40*k, y+10*k, 30*k, 10*k), 0)
        ellipse(screen, (128, 128, 128), (x-60*k, y-30*k, 30*k, 60*k), 0)
        ellipse(screen, (128, 128, 128), (x-20*k, y-10*k, 30*k, 60*k), 0)
        ellipse(screen, (128, 128, 128), (x-70*k, y+20*k, 30*k, 10*k), 0)
        ellipse(screen, (128, 128, 128), (x-30*k, y+40*k, 30*k, 10*k), 0)
        rect(screen, (128, 128, 128), (x-50*k, y-60*k, 50*k, 50*k), 0)
        rect(screen, (0, 0, 0), (x-50*k, y-60*k, 50*k, 50*k), 1)
        ellipse(screen, (255, 0, 0), (x-30*k, y-30*k, 10*k, 17*k), 0)
        ellipse(screen, (128, 128, 128), (x-40*k, y-50*k, 30*k, 30*k), 0)
        ellipse(screen, (0, 0, 0), (x-40*k, y-50*k, 30*k, 30*k), 1)
        rect(screen, (128, 128, 128), (x-40*k, y-50*k, 30*k, 20*k), 0)
        ellipse(screen, (128, 128, 128), (x-60*k, y-60*k, 20*k, 20*k), 0)
        ellipse(screen, (0, 0, 0), (x-60*k, y-60*k, 20*k, 20*k), 1)
        ellipse(screen, (128, 128, 128), (x-10*k, y-60*k, 20*k, 20*k), 0)
        ellipse(screen, (0, 0, 0), (x-10*k, y-60*k, 20*k, 20*k), 1)   
        ellipse(screen, (255, 255, 255), (x-40*k, y-50*k, 10*k, 6*k), 0)
        ellipse(screen, (0, 0, 0), (x-40*k, y-50*k, 10*k, 6*k), 1)
        ellipse(screen, (255, 255, 255), (x-20*k, y-50*k, 10*k, 6*k), 0)
        ellipse(screen, (0, 0, 0), (x-20*k, y-50*k, 10*k, 6*k), 1)
        ellipse(screen, (0, 0, 0), (x-37*k, y-50*k, 4*k, 6*k), 0)
        ellipse(screen, (0, 0, 0), (x-17*k, y-50*k, 4*k, 6*k), 0)
################################################################################

rect(screen, (51, 255, 255), (0, 0, 400, 280), 0)  #nebo
rect(screen, (102, 255, 51), (0, 280, 400, 280), 0)  #trava

draw_zabor(0, 80, 1)
draw_dom(280, 390, 1)
draw_sobaka(100, 480, 1, False)

################################################################################

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
