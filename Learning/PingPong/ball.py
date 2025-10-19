from turtle import Turtle




class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.2, stretch_len=0.2)
        self.penup()
        self.color("white")
        self.speed(2)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
       # self.x_move *= -1