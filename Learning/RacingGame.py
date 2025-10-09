from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

#turtles
colors = ["red", "green", "blue", "yellow", "purple"]
turtles = []

#pos
start_x = -350
start_y = 150
space = 100 #vertical space between turtles


Turtle_choice = input("Which turtle would you like to play?")

for i in range(4):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(start_x, start_y - i * space)
    turtles.append(t)

screen.update()

race_on = True

while race_on:
    for t in turtles:
        t.forward(random.randint(5, 15))

        if t.xcor() >= 350:
            race_on = False
            winner_color = t.color()
            print(f"{winner_color} wins!")
            break
    screen.update()





screen.bye()