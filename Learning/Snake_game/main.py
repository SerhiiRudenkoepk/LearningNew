from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]
snakes = []
'''
This for loop is making things much easier to read and shorter than an example bellow.

snake2 = Turtle(shape="square")
snake2.color("white")
snake2.goto(-20, 0)
snake3 = Turtle(shape="square")
snake3.color("white")
snake3.goto(-40,0)

'''

# for each position in starting position we're creating those turtles
for position in starting_position:
    snake1 = Turtle(shape="square")
    snake1.color("white")
    snake1.goto(position)
    snakes.append(snake1)
    snake1.pencolor("black")



game_is_on = True

while game_is_on:
    screen.update()
    for snk in snakes:
        snk.forward(20)
        time.sleep(1)






screen.exitonclick()