from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RANGES = [y for y in range(-240, 260, 20)]
NUMBER_OF_CARS = 30


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.create_cars()


    def create_cars(self):
        for _ in range(NUMBER_OF_CARS):
            car = Turtle('square')
            car.hideturtle()
            car.color(choice(COLORS))
            car.pu()
            car.setheading(180)
            car.shapesize(1, 2, 1)
            car.goto(choice(RANGES), choice(RANGES))
            car.showturtle()
            self.cars.append(car)

    def move(self, speed):
        for car in range(NUMBER_OF_CARS):
            self.cars[car].forward(speed)
            if self.cars[car].xcor() < - 320:
                self.start_from_right(self.cars[car])

    def start_from_right(self, car):
        car.hideturtle()
        car.goto(300, choice(RANGES))
        car.showturtle()
        

