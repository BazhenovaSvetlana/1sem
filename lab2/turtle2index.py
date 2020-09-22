import turtle as t
import math as m

t.shape('turtle')
line = 20

def odin():
    t.left(45)
    t.forward(m.sqrt(2)*line)
    t.right(135)
    t.forward(2 * line)
    t.left(90)

def chetiri():
    t.right(90)
    t.forward(line)
    t.left(90)
    t.forward(line)
    t.left(90)
    t.forward(line)
    t.left(180)
    t.forward(2*line)
    t.left(90)
    
    
def nol():
    t.right(90)
    t.forward(2*line)
    t.left(90)
    t.forward(line)
    t.left(90)
    t.forward(2*line)
    t.left(90)
    t.forward(line)
    t.left(180)

def sem():
    t.forward(line)
    t.right(135)
    t.forward(m.sqrt(2)*line)
    t.left(45)
    t.forward(line)
    t.left(90)
    

odin()

t.penup()
t.forward(line*0.25)
t.left(90)
t.forward(2*line)
t.right(90)
t.pendown()

chetiri()

t.penup()
t.forward(line*0.25)
t.left(90)
t.forward(line)
t.right(90)
t.pendown()

odin()

t.penup()
t.forward(line*0.25)
t.left(90)
t.forward(2*line)
t.right(90)
t.pendown()

sem()

t.penup()
t.forward(line*1.25)
t.left(90)
t.forward(line*2)
t.right(90)
t.pendown()

nol()

t.penup()
t.forward(1.25*line)
t.pendown()

nol()