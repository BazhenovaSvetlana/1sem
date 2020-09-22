import turtle as t
t.shape('turtle')

def star(n):
    for i in range(n):
        t.forward(300)
        t.right(180 - 180/n)

n = int(input())
star(n)


