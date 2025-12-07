from turtle import Turtle, Screen
import time
import snake
import food


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)


snake = snake.Snake()
food = food.Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True



while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)
    
    
    if snake.head.distance(food) < 14:
        food.refresh()




screen.exitonclick()