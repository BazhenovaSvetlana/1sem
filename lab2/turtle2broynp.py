import turtle as t
import random as r

t.shape('circle')

for i in range(1000):
    t.forward(r.randint(10, 30))
    t.left(r.randint(0, 360))
        
