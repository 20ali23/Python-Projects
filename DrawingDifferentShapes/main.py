#Gerekli kütüphanelerin içe aktarılması
from turtle import Turtle, Screen
import random

#Kaplumbağa nesnesi oluşturma
turtle = Turtle()

#Renk listesi oluşturma
colours = ["Black", "Blue", "Yellow", "Green", "Orange"]

#Şekilleri çizme
for i in range(3, 10):
    angle = 360 / i
    for _ in range(i):
        turtle.color(random.choice(colours))
        turtle.forward(100)
        turtle.right(angle)

screen = Screen()
screen.exitonclick