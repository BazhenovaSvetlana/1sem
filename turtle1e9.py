import turtle as t
import math as m

t.shape('turtle')



def draw_n(n, R):
    
    t.penup() #изначальтно черепашка в центре и смотрит вправо
    t.forward(R)
    t.pendown()
    
    a = 180 * ((n - 2) / n)   # это угол  в градусах
    f = 180 - a #угол поворота!!!!!!!!! в градусах
    x = 2 * R * m.sin(m.pi/n)  # это сторона 
    t.left(180 - (a / 2))  #первый поворот
    for i in range(n):
        t.forward(x)
        t.left(f)
    t.right(180 - (a / 2)) #последний поворот
    
    t.penup()
    t.backward(R)
    t.pendown()  #возвращаем черепашку в центр

count = int(input())
R = 10
for i in range (3, count+2):
    draw_n(i, R)
    R += 10
 
 
 #вложенные многоугольники 
