from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.pencolor("white")
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"score:{self.score}  high score:{self.high_score()}", align="center", font=FONT)

    def high_score(self):
        with open("data.txt") as file:
            new_highscore = file.read()
            return new_highscore
             
    def reset_scoreboard(self):
        try:
            if self.score > int(self.high_score()):
                with open("data.txt", "w") as file:
                    file.write(str(self.score))
        except ValueError:
            return None
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()