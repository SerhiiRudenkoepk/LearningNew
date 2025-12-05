from turtle import Turtle, Screen
import time
import snake

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)


snake = snake.Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True



while game_is_on:
    screen.update()
    for snk in snake.segments:
        snk.forward(20)
        time.sleep(0.1)




screen.exitonclick()