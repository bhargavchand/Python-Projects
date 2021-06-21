from turtle import Turtle


class Bar(Turtle):
    def __init__(self, x_corr, y_corr):
        super().__init__()
        self.shape("square")
        self.color("violet")
        self.shapesize(stretch_wid=5, stretch_len=1.2)
        self.penup()
        self.setposition(x_corr, y_corr)

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
