#Gerekli kütüphanelerin ve sınıfların içe aktarılması
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Ekran ayarları
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

#Sınıfları kullanarak nesne oluşturma
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

#Raketleri hareket ettirme
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")


game_is_one = True
while game_is_one:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Top üst duvara çarpmadan sıçratma
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Top rakete yaklaştığında zıplama
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.ycor() > -320:
        ball.bounce_x()

    #Top dışarı çıkarsa
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Top dışarı çıkarsa
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()