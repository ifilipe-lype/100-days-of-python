from turtle import Turtle

TEXT_ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()

        self.l_score = 0
        self.r_score = 0

        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align=TEXT_ALIGNMENT, font=FONT)

        self.goto(100, 200)
        self.write(f"{self.r_score}", align=TEXT_ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_board()

    def r_point(self):
        self.r_score += 1
        self.update_board()
