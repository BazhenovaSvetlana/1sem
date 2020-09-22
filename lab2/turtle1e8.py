import turtle as t
t.shape('turtle')
def line_2(size):
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)


s = 10
for i in range(1000):
    line_2(s)
    s += 10
    
#квадратная спираль
