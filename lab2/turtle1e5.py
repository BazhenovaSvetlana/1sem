import turtle 
turtle.shape('turtle')
def kvadrat(size):
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.pendown()


n =  int(input())
s = 10
for i in range(n):
    kvadrat(s)
    s += 20
    
    

