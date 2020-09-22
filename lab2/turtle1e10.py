import turtle as t
t.shape('turtle')

n = int(input())
for i in range(n):
    t.circle(50, 360)
    t.left(360 / n)
