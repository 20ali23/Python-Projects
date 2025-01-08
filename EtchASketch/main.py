#Gerekli kütüphanelerin içe aktarılması
from turtle import Turtle, Screen

#Kaplumbağa ve Ekran nesnesi oluşturma
tim = Turtle()
screen = Screen()

#İleri gitme işlevi
def move_forwards():
    tim.forward(10)

#Sola gitme işlevi
def turn_left():
    new_heading = tim.heading() +10
    tim.setheading(new_heading)

#Sağa gitme işlevi
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

#Geri gitme işlevi
def move_backwards():
    tim.backward(10)

#EKranı temizleme işlevi
def clear():
    tim.clear()
    tim.penup()
    tim.goto(0, 0)
    tim.pendown()
    tim.setheading(0)

#Kullanıcıyı dinleme
screen.listen()

screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="D", fun=turn_left)
screen.onkey(key="A", fun=turn_right)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="C", fun=clear)

#Ekrana tıklayarak kapatma
screen.exitonclick()