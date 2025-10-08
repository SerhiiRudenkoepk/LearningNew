from turtle import Turtle, Screen


screen = Screen()
timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("black")
screen.setup(800, 600)

# timmy.pendown()

def move_forward ():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def move_left():
    timmy.left(4)

def move_right():
    timmy.right(4)

def stop_drawing():
    timmy.penup()

def start_drawing():
    timmy.pendown()


screen.onkey(key="space", fun=move_forward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="w", fun=start_drawing)
screen.onkey(key="s", fun=stop_drawing)
screen.listen()


screen.exitonclick()