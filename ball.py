from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(1)
        self.pu()
        self.color("white")
        self.shape("circle")
        self.setposition(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def start_move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.setposition(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
        self.bounce_y()
        self.start_move()
