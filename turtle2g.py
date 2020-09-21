import turtle as t
x_max, y_max = 1000, 100



ay = -10
dt = 0.1

x, y, Vx, Vy = 0, 0, 10, 0

while True:
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2 
    Vy += ay*dt
    t.goto(x, y)
    if abs(y) >= y_max:
        Vy *= -1
    if abs(x) >= x_max:
        Vx *= -1
    