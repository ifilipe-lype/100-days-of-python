from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Cursive", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = 0

        try:
            with open(".high_score.txt") as score_file:
                self.high_score = int(score_file.read())
        except:
            with open(".high_score.txt", "w") as score_file:
                score_file.write("0")

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open(".high_score.txt", mode="w") as score_file:
                score_file.write(f"{self.high_score}")

        self.score = 0

        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

