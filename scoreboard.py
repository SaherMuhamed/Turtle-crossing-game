from turtle import Turtle

FONT = ("Courier", 18, "bold")
COLOR = "#141E27"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.color(COLOR)
        self.goto(x=-270, y=170)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increment_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)

    def win(self):
        self.goto(0, 0)
        self.write("You Win!", align="center", font=FONT)
