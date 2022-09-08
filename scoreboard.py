from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.color("teal")
        self.pu()
        self.player_1_score = 0
        self.player_2_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"Player 1: {self.player_1_score}", align="center", font=("Courier", 18, "normal"))
        self.goto(100, 200)
        self.write(f"Player 2: {self.player_2_score}", align="center", font=("Courier", 18, "normal"))

    def player_2_point(self):
        self.player_2_score += 1
        self.update_score()

    def player_1_point(self):
        self.player_1_score += 1
        self.update_score()
