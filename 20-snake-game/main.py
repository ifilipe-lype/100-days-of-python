from turtle import Screen, Turtle

screen = Screen()

# screen setup
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake_game")

# initial snake's body
starting_position = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_position:
    segment = Turtle("square")
    segment.color("white")
    segment.goto(position)


screen.exitonclick()
