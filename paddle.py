from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1, 1)

    def move_up(self):
        if self.ycor() <= 300:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() >= -300:
            self.sety(self.ycor() - 20)

    def set_paddle_1(self):
        self.setposition(350, 0)

    def set_paddle_2(self):
        self.setposition(-350, 0)




