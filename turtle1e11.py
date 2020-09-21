import turtle as t
t.shape('turtle')
t.speed(0)
t.left(90)


k = 20
n = int(input())
for i in range (1, n + 1):
    t.circle(k, 360)
    k += 10
    
t.left(180)


k = 20
for i in range (1, n + 1):
    t.circle(k, 360)
    k += 10