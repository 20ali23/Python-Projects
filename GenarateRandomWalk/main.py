#Gerekli kütüphanelerin içe aktarılması
from turtle import Turtle, Screen
import random

#Kaplumbağa nesnesi oluşturma
turtle = Turtle()

#Renk listesi
colours = ["Black", "Blue", "Yellow", "Green", "Orange"]

#Yön listesi
directions = [0, 90, 180, 270]

#Genişlik ayarlama
turtle.pensize(15)

#Hız ayarlama
turtle.speed("fastest")

#Rastgele hareket etme
for _ in range(200):
    turtle.color(random.choice(colours))
    turtle.forward(30)
    turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()