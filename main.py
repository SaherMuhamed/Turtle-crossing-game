import random
import time
from turtle import Screen
from scoreboard import Scoreboard
from crossing_turtle import TurtleCrossing
from cars import CarManager

# TODO 1: Create the setup screen.
# Setting up the screen
screen = Screen()
screen.tracer(0)
screen.bgpic("street.png")
screen.setup(width=700, height=400)
screen.title("Turtle Crossing")


crossing_turtle = TurtleCrossing()
scoreboard = Scoreboard()

# TODO 2: Make the turtle moves.
screen.listen()
screen.onkeypress(fun=crossing_turtle.move_up, key="Up")
screen.onkeypress(fun=crossing_turtle.move_down, key="Down")
screen.onkeypress(fun=crossing_turtle.move_right, key="Right")
screen.onkeypress(fun=crossing_turtle.move_left, key="Left")


all_cars = []
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    random_chances = random.randint(1, 6)
    if random_chances == 1:
        cars = CarManager()
        all_cars.append(cars)
    for car in all_cars:
        car.moving()
        # TODO 3: Detect the collision with cars.
        if car.distance(crossing_turtle) < 30:
            game_is_on = False
            scoreboard.game_over()

        # TODO 4: Detect if the turtle cross the road.
        for x_cor in range(-350, 350):
            if crossing_turtle.distance(x=x_cor, y=190) < 15:
                # game_is_on = False
                # car.speed_up()
                # print(car.speed_up())
                crossing_turtle.goto(x=0, y=-175)
                scoreboard.increment_level()


screen.exitonclick()
