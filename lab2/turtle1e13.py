import turtle as t
t.shape('circle')

t.penup()                 
t.goto(100, 0)
t.pendown()

t.left(90)
t.color('black', 'yellow')
t.begin_fill()
t.circle(100,360)
t.end_fill()

t.penup()                 
t.goto(30, 30)
t.pendown()
t.color('blue')
t.stamp()

t.penup()                 
t.goto(-30, 30)
t.pendown()
t.color('blue')
t.stamp()

t.penup()                 
t.goto(0, 10)
t.pendown()
t.width(10)
t.color('black')
t.goto(0, -20)

t.penup()                 
t.goto(-30, -40)
t.pendown()

t.color('red')
t.left(180)
t.circle(30,180)

