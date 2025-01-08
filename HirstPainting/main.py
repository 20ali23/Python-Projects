#Gerekli kütüphanelerin içe aktarılması
import turtle as turtle_module
import random
import colorgram

#Renk kodları için boş liste oluşturma
rgb_colors = []

#Kullanılacak resimdeki renklerin adet sayısı kadar kodunu çıkarma
colors = colorgram.extract('20_001.jpg', 30)

#Renk kodlarını rgb tuple'a çevirme
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

#Renk modunu 255 yapma
turtle_module.colormode(255)

#Kaplumbağa sınıfından nesne oluşturma
tim = turtle_module.Turtle()

#Resimdeki renklerin rgb kod listesi
color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

#Kaplumbağayı görünmez yapma
tim.hideturtle()

#Kaplumbağanın kafasını çevirme
tim.setheading(210)

#Kalemi kaldırma
tim.penup()

tim.forward(300)
tim.setheading(360)

#Kaplumbağanın hızını ayarlama
tim.speed("fastest")

#Kaplumbağayı kullanarak resim çizme
for _ in range (10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)

screen = turtle_module.Screen()
screen.exitonclick()