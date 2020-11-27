import pygame
pygame.init()
FPS = 30
screen = pygame.display.set_mode((500, 700))
screen.fill(pygame.Color(82, 109, 103),pygame.Rect(0, 0, 500, 700))


def car(x,y,r,ori):
    if ori == 'right':
        pygame.draw.ellipse(screen, (0, 0, 0), (x-int(20*r), y+int(30*r), int(r*40), int(r*10)))
        pygame.draw.rect(screen, (0, 205, 255), (x, y, int(240*r), int(40*r)))
        pygame.draw.rect(screen, (0, 205, 255), (x+int(40*r), y-int(30*r), int(120*r), int(70*r)))
        pygame.draw.rect(screen, (255, 255, 255), (x+int(50*r), y-int(20*r), int(40*r), int(20*r)))
        pygame.draw.rect(screen, (255, 255, 255), (x+int(110*r), y-int(20*r), int(40*r), int(20*r)))
        pygame.draw.ellipse(screen, (0, 0, 0), (x+ int(20*r), y+int(20*r), int(r*40), int(r*40)))
        pygame.draw.ellipse(screen, (0, 0, 0), (x+int(180*r), y+ int(20*r), int(r*40), int(r*40)))
    else:
        pygame.draw.ellipse(screen, (0, 0, 0), (x-int(20*r), y+int(30*r), int(r*40), int(r*10)))
        pygame.draw.rect(screen, (0, 205, 255), (x-int(240*r), y, int(240*r), int(40*r)))
        pygame.draw.rect(screen, (0, 205, 255), (x-int(160*r), y-int(30*r), int(120*r), int(70*r)))
        pygame.draw.rect(screen, (255, 255, 255), (x-int(150*r), y-int(20*r), int(40*r), int(20*r)))
        pygame.draw.rect(screen, (255, 255, 255), (x-int(90*r), y-int(20*r), int(40*r), int(20*r)))
        pygame.draw.ellipse(screen, (0, 0, 0), (x-int(220*r), y+int(20*r), int(r*40), int(r*40)))
        pygame.draw.ellipse(screen, (0, 0, 0), (x-int(60*r), y+int(20*r), int(r*40), int(r*40)))        

def fon(x,y,r,ori):
    if ori == 'right':
        pygame.draw.rect(screen, (255, 255, 255), (x, y, int(300*r), int(240*r)))
        pygame.draw.rect(screen, (184, 197, 201), (x+int(5*r), y+int(5*r), int(290*r), int(230*r)))
        pygame.draw.rect(screen, (148, 168, 173), (x+int(20*r), y+int(20*r), int(60*r), int(240*r)))
        pygame.draw.rect(screen, (148, 173, 168), (x+int(90*r), y+int(30*r), int(60*r), int(240*r)))
        pygame.draw.rect(screen, (184, 201, 197), (x+int(60*r), y+int(70*r), int(70*r), int(230*r)))
        pygame.draw.rect(screen, (220, 228, 227), (x+int(210*r), y+int(10*r), int(60*r), int(240*r)))
        pygame.draw.rect(screen, (112, 146, 139), (x+int(180*r), y+int(80*r), int(60*r), int(230*r)))        
    else:
        pygame.draw.rect(screen, (255, 255, 255), (x-300*r, y, int(300*r), int(240*r)))
        pygame.draw.rect(screen, (184, 197, 201), (x-int(295*r), y+int(5*r), int(290*r), int(230*r)))
        pygame.draw.rect(screen, (148, 168, 173), (x-int(80*r), y+int(20*r), int(60*r), int(240*r)))
        pygame.draw.rect(screen, (148, 173, 168), (x-int(150*r), y+int(30*r), int(60*r), int(240*r)))
        pygame.draw.rect(screen, (184, 201, 197), (x-int(130*r), y+int(70*r), int(70*r), int(230*r)))
        pygame.draw.rect(screen, (220, 228, 227), (x-int(270*r), y+int(10*r), int(60*r), int(240*r)))
        pygame.draw.rect(screen, (112, 146, 139), (x-int(240*r), y+int(80*r), int(60*r), int(230*r)))        
    

def cloud(x, y, r1, r2):
    surf_1 = pygame.Surface((x, y), pygame.SRCALPHA)
    pygame.draw.ellipse(surf_1, (0, 0, 0, 100), (0, 0, r1, r2))
    screen.blit(surf_1, (x, y))

def cloud_t(x, y, r1, r2):
    surf_1 = pygame.Surface((x, y), pygame.SRCALPHA)
    pygame.draw.ellipse(surf_1, (255, 255, 255, 7), (0, 0, r1, r2))
    screen.blit(surf_1, (x, y))


def tyman(x, y, r1, r2): #i putalas
    i = 0
    while r2 > 0:
        i += 1
        cloud_t(x, y, r1, r2)
        x += i
        y += i
        r1 -= 2*i
        r2 -= 2*i

################################################
    
    
fon(350, 0, 1.37, 'right')
fon(410, 0, 1.37, 'left')
cloud(250, 100, 250, 100)
cloud(150, 70, 150, 70)
fon(500, 170, 1, 'left')
fon(0, 185, 1, 'right')
car(100, 500, 0.35,'left')
car(240, 520, 0.35,'left')
car(360, 500, 0.35,'left')
car(480, 520, 0.35,'left')
car(50, 580, 1,'right')
car(480, 640, 1,'left')
tyman(200, 560, 200, 130)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()