import random
from turtle import Turtle, Screen

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X = 370
CARS = ["cars_images/Red.gif", "cars_images/Cyan.gif", "cars_images/Blue.gif", "cars_images/Green.gif",
        "cars_images/Purple.gif", "cars_images/Yellow.gif", "cars_images/White.gif", "cars_images/Black.gif"]

screen = Screen()
for _ in CARS:
    screen.addshape(_)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.penup()
        self.setheading(180)
        self.random_generate()
        random_y = random.randint(-150, 150)
        self.goto(x=STARTING_X, y=random_y)

    def random_generate(self):
        self.shape(random.choice(CARS))

    def moving(self):
        self.setheading(to_angle=180)
        self.forward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
        self.speed(self.car_speed)
