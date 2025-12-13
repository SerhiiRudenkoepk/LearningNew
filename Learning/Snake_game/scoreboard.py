from turtle import Turtle
from pathlib import Path

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        try:
            with open("data.txt", mode="r") as file:
                content = file.read()
                self.high_score = int(content) if content.strip() else 0
        except FileNotFoundError:
            self.high_score = 0
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score)) # writing a high_score in this file
        self.score = 0
        self.update_scoreboard()



    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
