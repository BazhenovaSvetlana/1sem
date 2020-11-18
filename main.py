import pygame
import numpy as np
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 700))

#цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#функция создания случайного шарика
class Ball:
    vx = 0
    vy = 0
    x = 0
    y = 0
    r = 0
    color = BLACK
    def new(self):
        a = randint(0, 360)
        self.vx = 5 * np.cos(2 * np.pi * a / 360)
        self.vy = 5 * np.sin(2 * np.pi * a / 360)
        self.x = randint(50, 1150)
        self.y = randint(50, 650)
        self.r = randint(30, 50)
        self.color = COLORS[randint(0, 5)]
    pass

#класс квадратов
class Quad:
    v = 0 #скорость квадрата
    a = 0 #движение квадрата (горизонтально, вертикально)
    x = 0 #координата центра квадрата по х
    y = 0 #координата центра квадрата по у
    r = 0 #сторона квадрата
    color = BLACK
    def new (self):
        self.v = randint(3, 10)
        self.a = randint(0, 1)
        self.x = randint(100, 1100)
        self.y = randint(60, 640)
        self.r = randint(30, 60)
        self.color = COLORS[randint(0, 5)]
    def draw (self): #квадрат
        polygon(screen, self.color, ((self.x - self.r//2, self.y - self.r/2),
                                     (self.x + self.r//2, self.y - self.r/2),
                                     (self.x + self.r//2, self.y + self.r//2),
                                     (self.x - self.r//2, self.y + self.r//2),
                                     (self.x - self.r//2, self.y - self.r/2)))


def click(event):
    print(x, y, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
k = 0
print('имя игрока') #имя нужно для  статистики
name = str(input())
j = randint(2, 5) #количество шаров
balls_list = list() #список шаров
for i in range(0, j):
    ball = Ball()
    ball.new()
    balls_list.append(ball)
l = randint(1, 4) #количество квадратов
quads_list = list() #список квадратов
for i in range(0, l):
    quad = Quad()
    quad.new()
    quads_list.append(quad)
while not finished:
    for m in range(FPS):
        clock.tick(FPS)
        #перерисовываем каждый шар из списка
        for i in range(j):
            x = balls_list[i].x
            y = balls_list[i].y
            vx = balls_list[i].vx
            vy = balls_list[i].vy
            r = balls_list[i].r
            color = balls_list[i].color
            #угол отражения шарика
            b = randint(1, 89)
            if (0 > y - r) | (y + r > 900):
                 vy = -vy / (vy**2)**0.5 * 5 * np.sin(2*np.pi/360 * b)
                 vx = vx / (vx**2)**0.5 * 5 * np.cos(2*np.pi/360 * b)
            if (0 > x - r) | (x + r > 1200):
                vy = vy / (vy ** 2) ** 0.5 * 5 * np.sin(2 * np.pi / 360 * b)
                vx = -vx / (vx ** 2) ** 0.5 * 5 * np.cos(2 * np.pi / 360 * b)
            x = int(x + vx)
            y = int(y + vy)
            circle(screen, color, (int(x), int(y)), r) #заново рисуем шарик
            balls_list[i].x = x
            balls_list[i].y = y
            balls_list[i].vx = vx
            balls_list[i].vy = vy
            balls_list[i].r = r
        #перерисовываем все квадраты
        for i in range(l):
             x = quads_list[i].x
             y = quads_list[i].y
             v = quads_list[i].v
             a = quads_list[i].a
             r = quads_list[i].r
             color = quads_list[i].color
             x = int(x + a * v * (-1)**(int(m/10)))
             y = int(y + (1-a) * v * (-1)**(int(m/6)))
             quads_list[i].draw()
             quads_list[i].x = x
             quads_list[i].y = y
             quads_list[i].v = v
             quads_list[i].r = r
        pygame.display.update() #обновление экрана
        screen.fill(BLACK)
        #нажатие мышкой
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Click!')
                click(event)
                for i in range(j):
                    x = balls_list[i].x
                    y = balls_list[i].y
                    r = balls_list[i].r
                    if (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 < r**2:
                        k += 1 #если попали, + очко
                for i in range (l):
                     x = quads_list[i].x
                     y = quads_list[i].y
                     r = quads_list[i].r
                     if (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 < (r/2+10)**2:
                         k += 2 #если попали, + 2 очка
    j = randint(2, 5)
    balls_list = list()
    for i in range(0, j):
         ball = Ball()
         ball.new()
         balls_list.append(ball)
    l = randint(1, 4)
    quads_list = list()
    for i in range(0, l):
         quad = Quad()
         quad.new()
         quads_list.append(quad)
    pygame.display.update()
    screen.fill(BLACK)
print(k)
pygame.quit()

#добавим баллы в статистику
inp = open('1.txt', 'r')
a = inp.readlines()
#в списке: четные элементы - имена игроков, нечетные - кол-во баллов
b = list()
for i in range(len(a)):
    b.extend(a[i].split())
#список с баллами
c = list()
for i in range(int(len(b)/2)):
    c.append(int(b[2*i+1]))
i = 0
s = 0
#место игрока
while s == 0 and i < int(len(c)):
    if c[i] > k:
        i+=1
    else:
        s = 1
b.insert(2*i, name)
b.insert(2*i+1, str(k))
inp.close()
out = open('1.txt', 'w')
for i in range(len(a)+1):
    out.write(b[2*i] + ' ')
    out.write(b[2*i+1] + '\n')
out.close()