import time
import turtle
from turtle import Turtle, Screen
from bar import Bar
from ball import Ball
from score import Score

my_screen = Screen()
my_screen.tracer(0)
my_screen.bgcolor("black")
my_screen.setup(height=600, width=800)
my_screen.title("Ping-Pong")

bar1 = Bar(350, 0)
bar2 = Bar(-350, 0)
ball = Ball()
scoreBoard = Score()

my_screen.listen()

my_screen.onkey(bar1.move_up, 'Up')
my_screen.onkey(bar1.move_down, 'Down')
my_screen.onkey(bar2.move_up, 'w')
my_screen.onkey(bar2.move_down, 's')

is_game_running = True

while is_game_running:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(bar1) < 50 and ball.xcor() > 320 or ball.distance(bar2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreBoard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreBoard.r_point()

my_screen.exitonclick()
