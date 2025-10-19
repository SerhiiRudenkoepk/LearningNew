import turtle
from turtle import Turtle, Screen
import random
import players
import ball


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
ball = ball.Ball()

# Calling out class and functions from players.py
pong_players = players.Players()
pong_players.pl1()
pong_players.pl2()


# Creating functions where it will add +20 and -20 to ycord.
def go_up():
    new_y = pong_players.player1.ycor() + 20
    pong_players.player1.goto(pong_players.player1.xcor(), new_y)

# Not using pong_players.player1.pl1 - because player1 - already our turtle.
def go_down():
    new_y = pong_players.player1.ycor() - 20
    pong_players.player1.goto(pong_players.player1.xcor(), new_y)

# Moving Up and Down by pressing associated buttons
screen.listen()
screen.onkey(key="Up", fun=go_up)
screen.onkey(key="Down", fun=go_down)

game_on = True
while game_on:
    screen.update()
    ball.move()

    # Collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()





screen.exitonclick()