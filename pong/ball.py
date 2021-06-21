from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.move_speed = 0.1
        self.xmove = 5
        self.ymove = 5

    def move(self):
        new_xcorr = self.xcor() + self.xmove
        new_ycorr = self.ycor() + self.ymove
        self.goto(new_xcorr, new_ycorr)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
