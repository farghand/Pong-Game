from turtle import Screen, Turtle
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

game_is_on = True

paddle_1 = Paddle()
paddle_1.set_paddle_1()

paddle_2 = Paddle()
paddle_2.set_paddle_2()

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.start_move()

    # Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with both paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if paddle misses ball
    if ball.xcor() > 380:
        # Player 2 gets a point
        ball.reset_position()
        scoreboard.player_2_point()

    if ball.xcor() < -380:
        # Player 1 gets a point
        speed = 0.1
        ball.reset_position()
        scoreboard.player_1_point()

screen.exitonclick()
