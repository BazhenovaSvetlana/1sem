import turtle as t
import math as m


t.shape('turtle')


def step(phi):
    phi = phi * m.pi / 180
    l = 1 * (phi * m.sqrt(1 + phi ** 2) + m.log (phi + m.sqrt(1 + phi ** 2)))
    t.forward(l)
    t.left(10)
    
for i in range(1000):
    step(i)



#спираль
