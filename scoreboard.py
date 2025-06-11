from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.goto(x=0, y=260)
        self.pencolor("white")
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"score:{self.score}  high score:{self.highscore}", align="center", font=FONT)
    
    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()