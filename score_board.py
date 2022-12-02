from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        with open("data") as high_score_data:
            self.high_score = int(high_score_data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 180)

    def score_board(self):
        self.write(f"SCORE: {self.scores}   High Score: {self.high_score}", align="center",
                   font=("Courier", 10, "normal"))

    def score_update(self):
        self.clear()
        self.scores += 1
        self.write(f"SCORE: {self.scores}   High Score: {self.high_score}", align="center",
                   font=("Courier", 10, "normal"))

    def h(self):
        self.clear()
        self.write(f"SCORE: {self.scores}   High Score: {self.high_score}", align="center",
                   font=("Courier", 10, "normal"))

    def reset(self):
        if self.scores > self.high_score:
            self.high_score = self.scores
            with open("data", mode="w") as high_score_data:
                high_score_data.write(f"{self.high_score}")
        self.scores = 0
        self.h()

    #def game_over(self):
        #self.goto(0, 0)
        #self.write("GAME OVER", align="center", font=("Courier", 20, "normal"))



