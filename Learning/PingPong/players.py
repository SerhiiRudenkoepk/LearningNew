from turtle import Turtle, Screen
import random

class Players:
    def __init__(self):
        pass
    def pl1(self):
        self.player1 = Turtle(shape="square")
        self.player1.color("white")
        self.player1.shapesize(stretch_wid=1, stretch_len=5)
        self.player1.penup()
        self.player1.goto(350, 0)
        self.player1.setheading(90)
        self.player1.speed("fastest")

    def pl2(self):
        self.player2 = Turtle(shape="square")
        self.player2.color("white")
        self.player2.shapesize(stretch_wid=1, stretch_len=5)
        self.player2.penup()
        self.player2.goto(-350, 0)
        self.player2.setheading(90)
        self.player2.speed("fastest")

