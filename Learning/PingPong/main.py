from turtle import Turtle, Screen
import random
import players

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")





def npc1():
    pass




pong_players = players.Players()
pong_players.pl1()
pong_players.pl2()
screen.exitonclick()