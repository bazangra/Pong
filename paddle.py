from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coord):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.turtlesize(5, 2)
        self.penup()
        self.goto(coord)

    def up(self):
        self.goto(self.xcor(), (self.ycor() + 50))

    def down(self):
        self.goto(self.xcor(), (self.ycor() - 50))