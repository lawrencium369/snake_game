from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(x=0, y=260)
        self.pencolor("white")
        self.updtae_scoreboard()
    
    def updtae_scoreboard(self):
        self.write(arg=f"score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.pencolor("white")
        self.write(arg=f"GAMEOVER\n", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.updtae_scoreboard()