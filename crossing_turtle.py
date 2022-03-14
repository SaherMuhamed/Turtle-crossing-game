from turtle import Screen, Turtle

STARTING_POSITION = (0, -175)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 170

screen = Screen()
screen.addshape("turtle.gif")


class TurtleCrossing(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle.gif")
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        y = self.ycor()
        y += MOVE_DISTANCE
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= MOVE_DISTANCE
        self.sety(y)

    def move_right(self):
        x = self.xcor()
        x += MOVE_DISTANCE
        self.setx(x)

    def move_left(self):
        x = self.xcor()
        x -= MOVE_DISTANCE
        self.setx(x)
