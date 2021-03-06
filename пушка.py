from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
all_points = 0

class Ball:
    def __init__(self, x=40, y=450):
        """ РљРѕРЅСЃС‚СЂСѓРєС‚РѕСЂ РєР»Р°СЃСЃР° Ball

        Args:
        x - РЅР°С‡Р°Р»СЊРЅРѕРµ РїРѕР»РѕР¶РµРЅРёРµ РјСЏС‡Р° РїРѕ РіРѕСЂРёР·РѕРЅС‚Р°Р»Рё
        y - РЅР°С‡Р°Р»СЊРЅРѕРµ РїРѕР»РѕР¶РµРЅРёРµ РјСЏС‡Р° РїРѕ РІРµСЂС‚РёРєР°Р»Рё
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coordinates(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """РџРµСЂРµРјРµСЃС‚РёС‚СЊ РјСЏС‡ РїРѕ РїСЂРѕС€РµСЃС‚РІРёРё РµРґРёРЅРёС†С‹ РІСЂРµРјРµРЅРё.

        РњРµС‚РѕРґ РѕРїРёСЃС‹РІР°РµС‚ РїРµСЂРµРјРµС‰РµРЅРёРµ РјСЏС‡Р° Р·Р° РѕРґРёРЅ РєР°РґСЂ РїРµСЂРµСЂРёСЃРѕРІРєРё. РўРѕ РµСЃС‚СЊ, РѕР±РЅРѕРІР»СЏРµС‚ Р·РЅР°С‡РµРЅРёСЏ
        self.x Рё self.y СЃ СѓС‡РµС‚РѕРј СЃРєРѕСЂРѕСЃС‚РµР№ self.vx Рё self.vy, СЃРёР»С‹ РіСЂР°РІРёС‚Р°С†РёРё, РґРµР№СЃС‚РІСѓСЋС‰РµР№ РЅР° РјСЏС‡,
        Рё СЃС‚РµРЅ РїРѕ РєСЂР°СЏРј РѕРєРЅР° (СЂР°Р·РјРµСЂ РѕРєРЅР° 800С…600).
        """
        canv.delete(self.id)
        self.x += self.vx
        self.y -= self.vy
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        if self.live < 0:
            balls.pop(balls.index(self))
            canv.delete(self.id)
        else:
                self.live -= 0.25
        if self.x - self.r <= 10:
            self.vx = -self.vx
            self.x = self.x + self.r + 10
        if self.x - self.r >= 790:
            self.vx = -self.vx
            self.x = self.x - self.r - 10
        if self.y - self.r <= 10:
            self.vy = -0.7 * self.vy
            self.y = self.y + self.r + 10
        if self.y - self.r >= 590:
            self.vy = -0.7 * self.vy
            self.y = self.y - self.r - 10

    def hit_test(self, obj):
        """Р¤СѓРЅРєС†РёСЏ РїСЂРѕРІРµСЂСЏРµС‚ СЃС‚Р°Р»РєРёРІР°Р»РєРёРІР°РµС‚СЃСЏ Р»Рё РґР°РЅРЅС‹Р№ РѕР±СЊРµРєС‚ СЃ С†РµР»СЊСЋ, РѕРїРёСЃС‹РІР°РµРјРѕР№ РІ РѕР±СЊРµРєС‚Рµ obj.

        Args:
            obj: РћР±СЊРµРєС‚, СЃ РєРѕС‚РѕСЂС‹Рј РїСЂРѕРІРµСЂСЏРµС‚СЃСЏ СЃС‚РѕР»РєРЅРѕРІРµРЅРёРµ.
        Returns:
            Р’РѕР·РІСЂР°С‰Р°РµС‚ True РІ СЃР»СѓС‡Р°Рµ СЃС‚РѕР»РєРЅРѕРІРµРЅРёСЏ РјСЏС‡Р° Рё С†РµР»Рё. Р’ РїСЂРѕС‚РёРІРЅРѕРј СЃР»СѓС‡Р°Рµ РІРѕР·РІСЂР°С‰Р°РµС‚ False.
        """
        if (obj.x-self.x)**2 + (obj.y-self.y)**2 <= (self.r+obj.r)**2:
            return True
        else:
            return False

class Gun:
    def __init__(self):
        """
        РљРѕРЅСЃС‚СЂСѓРєС‚РѕСЂ РєР»Р°СЃСЃР° Gun
        """
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Р’С‹СЃС‚СЂРµР» РјСЏС‡РѕРј.

        РџСЂРѕРёСЃС…РѕРґРёС‚ РїСЂРё РѕС‚РїСѓСЃРєР°РЅРёРё РєРЅРѕРїРєРё РјС‹С€Рё.
        РќР°С‡Р°Р»СЊРЅС‹Рµ Р·РЅР°С‡РµРЅРёСЏ РєРѕРјРїРѕРЅРµРЅС‚ СЃРєРѕСЂРѕСЃС‚Рё РјСЏС‡Р° vx Рё vy Р·Р°РІРёСЃСЏС‚ РѕС‚ РїРѕР»РѕР¶РµРЅРёСЏ РјС‹С€Рё.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targeting(self, event=0):
        """РџСЂРёС†РµР»РёРІР°РЅРёРµ. Р—Р°РІРёСЃРёС‚ РѕС‚ РїРѕР»РѕР¶РµРЅРёСЏ РјС‹С€Рё."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.new_target()

    def new_target(self):
        """ Р�РЅРёС†РёР°Р»РёР·Р°С†РёСЏ РЅРѕРІРѕР№ С†РµР»Рё. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        self.vx = rnd(-30, 30)
        self.vy = rnd(-30, 30)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self):
        """РџРѕРїР°РґР°РЅРёРµ С€Р°СЂРёРєР° РІ С†РµР»СЊ."""
        canv.coords(self.id, -10, -10, -10, -10)

    def move_target(self):
        """
        РџРµСЂРµРјРµСЃС‚РёС‚СЊ РјРёС€РµРЅСЊ РїРѕ РїСЂРѕС€РµСЃС‚РІРёРё РµРґРёРЅРёС†С‹ РІСЂРµРјРµРЅРё. РњРµС‚РѕРґ РѕРїРёСЃС‹РІР°РµС‚
        РїРµСЂРµРјРµС‰РµРЅРёРµ РјРёС€РµРЅРё Р·Р° РѕРґРёРЅ РєР°РґСЂ РїРµСЂРµСЂРёСЃРѕРІРєРё. РўРѕ РµСЃС‚СЊ, РѕР±РЅРѕРІР»СЏРµС‚
        Р·РЅР°С‡РµРЅРёСЏ self.x Рё self.y СЃ СѓС‡РµС‚РѕРј СЃРєРѕСЂРѕСЃС‚РµР№ self.vx Рё self.vy.
        """
        if self.live == 1:
            canv.delete(self.id)
            self.x += self.vx
            self.y -= self.vy
            self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
            )
            if self.x - self.r <= 100:
                self.vx = -self.vx
                self.x = self.x + self.r + 1
            if self.x - self.r >= 770:
                self.vx = -self.vx
                self.x = self.x - self.r - 1
            if self.y - self.r <= 100:
                self.vy = -0.7 * self.vy
                self.y = self.y + self.r + 1
            if self.y - self.r >= 570:
                self.vy = -0.7 * self.vy
                self.y = self.y - self.r - 1

t1 = Target()
t2 = Target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []

def points():
    global all_points, k
    canv.itemconfig(k, text=all_points)

def new_game(event=''):
    global g1, t1, t2, screen1, balls, bullet, all_points
    t1.new_target()
    t2.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targeting)
    t1.live = 1
    while t1.live or t2.live or balls:
        t1.move_target()
        t2.move_target()
        for b in balls:
            b.move()
            if b.hit_test(t1) and t1.live:
                t1.live = 0
                t1.hit()
            if b.hit_test(t2) and t2.live:
                t2.live = 0
                t2.hit()
            if t2.live == 0 and t1.live == 0:
                t2.hit()
                t1.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Р’С‹ СѓРЅРёС‡С‚РѕР¶РёР»Рё С†РµР»Рё Р·Р° ' + str(bullet) + ' РІС‹СЃС‚СЂРµР»РѕРІ')
        canv.update()
        time.sleep(0.03)
        g1.targeting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    all_points += 1
    points()
    canv.delete(g1)
    root.after(750, new_game)

k = canv.create_text(30, 30, text=all_points, font='28')
new_game()
tk.mainloop()