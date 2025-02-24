from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270,260)
        self.level = 1
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.clear()
        self.write(f"Level : {self.level}", align= "left",font=FONT)
        self.level += 1

    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)
    

