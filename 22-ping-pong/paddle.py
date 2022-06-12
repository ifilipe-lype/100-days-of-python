from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, 0)

    def move_up(self):
        new_y_pos = self.ycor() + 20
        if new_y_pos < 280:
            self.goto(x=self.xcor(), y=new_y_pos)

    def move_down(self):
        new_y_pos = self.ycor() - 20
        if new_y_pos > -280:
            self.goto(x=self.xcor(), y=new_y_pos)
