from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position, color, score_value):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.goto(position)
        self.score_value = score_value
        self.shapesize(stretch_wid=1.5, stretch_len=3)


