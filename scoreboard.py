import turtle
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.writeScore()
        # self.penup()

    def writeScore(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def addScore(self):
        self.score = self.score + 1

    def gameOver(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
