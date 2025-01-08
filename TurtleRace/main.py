#Gerekli kütüphanelerin içe aktarılması
from turtle import Turtle, Screen
import random

#Ekran nesnesi oluşturma
screen = Screen()

#Pencere boyunu belirleyip açma
screen.setup(width=500, height=400)

#Kullanıcıya soru penceresi açma
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

#Renl listesi oluşturma
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

#Kaplumbağa için y kordinatı listesi
y_positions = [-100, -50, 0, 50, 100, 150]

#Döngü kontrol değişkeni
is_race_on = False

#Boş liste
all_turtles = []

#Altı adet kaplumbağa oluşturma
for i in range(6):
    #Kaplumbağa nesnesi oluşturup şeklini verme
    new_turtle = Turtle(shape="turtle")
    #Kaplumbağa renk verme
    new_turtle.color(colors[i])
    #Kalemi kaldırma
    new_turtle.penup()
    #Kaplumbağayı kordinatına taşıma
    new_turtle.goto(x=-150, y=y_positions[i])
    #Kaplumbağayı listeye ekleme
    all_turtles.append(new_turtle)

#Giriş olup olmadığını kontrol etme
if user_bet:
    is_race_on = True

#Yarışı döngüye sokma
while is_race_on:

    #Kaplumbağaları döngüye sokma
    for turtle in all_turtles:

        #Kaplumbağanın x kordinatı 200'den büyük mü?
        if turtle.xcor() > 200:

            is_race_on = False
            #Kazanan kaplumbağanın rengine ulaşma
            winning_color = turtle.pencolor()
            #Kazana kaplumbağanın oyuncunun girdiği renk ile aynı olup olmadığını kontrol edip bildirme
            if winning_color == user_bet:
                print(f"You've win! The {winning_color} turtle is the winner!")

            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Kaplumbağayı rastgele hızına göre ilerletme
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()