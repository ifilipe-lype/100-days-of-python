import time
from turtle import Screen

from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pyng-pong")
screen.tracer(0)

scoreboard = Scoreboard()
right_paddle = Paddle(x_pos=350)
left_paddle = Paddle(x_pos=-350)
ball = Ball()

screen.listen()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() < - 380:
        scoreboard.r_point()
        ball.reset_position()

    elif ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

screen.exitonclick()
