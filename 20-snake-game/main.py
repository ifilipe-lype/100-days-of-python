from turtle import Screen, Turtle
import time

screen = Screen()

# screen setup
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake_game")
screen.tracer(0)

# initial snake's body
starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_position:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)

    segments.append(segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.5)
    head_segment = segments[0]
    head_segment.forward(20)

    for seg_idx in range(len(segments) - 1, 0, -1):
        segment = segments[seg_idx]
        next_segment = segments[seg_idx - 1]

        segment.goto(next_segment.position())


screen.exitonclick()
