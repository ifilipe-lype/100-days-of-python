from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x_pos = self.xcor() + 10
        new_y_pos = self.ycor() + 10

        self.goto(new_x_pos, new_y_pos)
