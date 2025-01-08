#Gerekli kütüphanelerin içe aktarılması
import turtle as t
import random                           

#Kaplumbağa nesnesi oluşturma
tim = t.Turtle()                  

#Kaplumbağa rengi için renk aralığı ayarlama
t.colormode(255)

#Rastgele rgb renk seçme
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

#Kaplumbağa hızını ayarlama
tim.speed("fastest")       

#Kaplumbağa ile daire oluşturma
tim.circle(100)

#Kaplumbağa ile 72 tane renkli daire oluşturma
for _ in range(72):
    tim.color(random_color())
    tim.right(5)               
    tim.speed("fastest")     
    tim.circle(100)            

#Kaplumbağa için ekran açma
screen = t.Screen()

#Ekrana tıklama ile kapatma
screen.exitonclick()