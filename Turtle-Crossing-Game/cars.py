"""Module to control the behaviour of cars."""

from random import choice
from turtle import Turtle
from const import (
    CAR_COLORS,
    CAR_STARTING_POS_X,
    CAR_STARTING_POS_Y,
    CAR_SPEED,
    CAR_X_RATIO, CAR_Y_RATIO
)

class Cars:
    """The cars class."""
    def __init__(self) -> None:
        self.all_cars: dict[Turtle] = {}

    def spawn_a_car(self) -> None:
        """Spawn a new car at the right end."""
        car_spawning_chance = choice([1, 2, 3, 4, 5])

        if car_spawning_chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(choice(seq=CAR_COLORS))
            new_car.shapesize(
                stretch_wid=CAR_Y_RATIO,
                stretch_len=CAR_X_RATIO
            )

            new_car.goto(
                x=CAR_STARTING_POS_X,
                y=choice(CAR_STARTING_POS_Y)
            )

            self.all_cars[new_car] = choice(seq=CAR_SPEED)

    def move_cars(self) -> None:
        """Make all cars to move."""
        for car, speed in self.all_cars.items():
            car.goto(
                x=car.xcor() - speed,
                y=car.ycor()
            )
