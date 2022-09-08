from turtle import *
from turtle import Turtle, Screen

setup = ""

def drag(i, j):
    tur.ondrag(None)
    tur.setheading(tur.towards(i, j))
    tur.goto(i, j)
    tur.ondrag(drag)

ws = Screen()
ws.title("kara tahta")
setup = input("arka plan rengini girin > ")
ws.bgcolor(setup)

tur = Turtle('circle')
tur.shapesize(0.5, 0.5, 0.5)
tur.speed('fastest')
setup = input("çizgi rengini girin > ")
tur.color(setup)     #e46e6f #82f8ad
tur.ondrag(drag)

done()

ws.mainloop()