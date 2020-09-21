import turtle as t

t.shape('turtle')
line = 20


def number_enter():
    t.penup()
    t.forward(line*0.25)
    t.pendown()

def draw_index(number):
    
    if number == 0:
        t.right(90)
        t.forward(2*line)
        t.left(90)
        t.forward(line)
        t.left(90)
        t.forward(2*line)
        t.left(90)
        t.forward(line)
        t.left(180)
        t.penup()
        t.forward(line)
        t.pendown()
        
    
    if number == 1:
        t.penup()
        t.right(90)
        t.forward(line)
        t.pendown()
        t.left(135)
        t.forward(2**0.5*line)
        t.right(135)
        t.forward(2 * line)
        t.penup()
        t.right(180)
        t.forward(2*line)
        t.pendown()
        t.right(90)
    
    
    if number == 2:
        t.forward(line)
        t.right(90)
        t.forward(line)
        t.right(45)
        t.forward(2**0.5*line)
        t.left(135)
        t.forward(line)
        t.penup()
        t.left(90)
        t.forward(2*line)
        t.right(90)
        t.pendown()


    if number == 3:
        t.forward(line) 
        t.right(135)
        t.forward(2**0.5*line)
        t.left(135)
        t.forward(line)
        t.right(135)
        t.forward(2**0.5*line)       
        t.penup()
        t.right(135)
        t.forward(2*line)
        t.right(90)
        t.forward(line)
        t.pendown()


    if number == 4:
        t.right(90)
        t.forward(line)
        t.left(90)
        t.forward(line)
        t.right(90)
        t.forward(line)
        t.left(180)
        t.forward(2*line)
        t.right(90)
    

    if number == 5:
        t.forward(line)
        t.left(180)
        t.forward(line)
        t.left(90)
        t.forward(line)
        t.left(90)
        t.forward(line)
        t.right(90)
        t.forward(line)
        t.right(90)
        t.forward(line)
        t.penup()
        t.right(90)
        t.forward(2*line)
        t.right(90)
        t.forward(line)
        t.pendown()
    

    if number == 6:
        t.penup()
        t.forward(line)
        t.pendown()
        t.right(135)
        t.forward(2**0.5*line)
        t.left(45)
        t.forward(line)
        t.left(90)
        t.forward(line)
        t.left(90)
        t.forward(line)
        t.left(90)
        t.forward(line)
        t.right(135)
        t.forward(2**0.5*line)
        t.right(45)
        

    if number == 7:
        t.forward(line)
        t.right(135)
        t.forward(2**0.5*line)
        t.left(45)
        t.forward(line)
        t.penup()
        t.left(90)
        t.forward(line)
        t.left(90)
        t.forward(2*line)
        t.pendown()
        t.right(90)
    

    if number == 8:
        t.right(90)
        t.forward(2*line)
        t.left(90)
        t.forward(line)
        t.left(90)
        t.forward(2*line)
        t.left(90)
        t.forward(line)
        t.left(90)
        t.forward(line)
        t.left(90)
        t.forward(line)
        t.left(90)
        t.forward(line)
        t.right(90)
    

    if number == 9:
        t.forward(line)
        t.right(90)
        t.forward(line)
        t.right(45)
        t.forward(2**0.5*line)
        t.right(180)
        t.forward(2**0.5*line)
        t.left(135)
        t.forward(line)
        t.right(90)
        t.forward(line)
        t.right(90)
        t.forward(line)
          
index = input()
for i in range(len(index)):
    draw_index(int(index[i]))
    number_enter()


