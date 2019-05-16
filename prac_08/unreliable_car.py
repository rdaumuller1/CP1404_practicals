
from random import randint
from prac_08.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)               # Gets the values from the car file
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)  # Gets the value from the car file
        return distance_driven
