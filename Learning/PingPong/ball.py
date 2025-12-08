from turtle import Turtle
import players




class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.2, stretch_len=0.2)
        self.penup()
        self.color("white")
        self.speed(1)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def is_collided_with(self, paddle):
        """Check if ball collides with a paddle"""
        # Check if ball is at the paddle's x position (with some tolerance)
        if abs(self.xcor() - paddle.xcor()) < 20:
            # Check if ball's y position is within the paddle's height range
            # Paddle is 5 units tall (stretch_len=5), so check ±50 pixels from center
            if abs(self.ycor() - paddle.ycor()) < 50:
                return True
        return False





    def bounce_y(self):
        """Bounce off top/bottom walls"""
        self.y_move *= -1
    
    def bounce_x(self):
        """Bounce off left/right walls or paddles"""
        self.x_move *= -1