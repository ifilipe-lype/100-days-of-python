import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake_game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    if snake.head_segment.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()

    if snake.head_segment.xcor() < -290 or snake.head_segment.xcor() > 290 or\
            snake.head_segment.ycor() < -290 or snake.head_segment.ycor() > 290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head_segment.distance(segment) <10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
