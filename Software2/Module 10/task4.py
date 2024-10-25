'''This exercise continues the previous car race exercise from the last exercise set. Write a Race class that has the
following properties: name, distance in kilometers and a list of cars participating in the race. The class has an
initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding
properties in the class. The class has the following methods:

hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of
speed for each car and calls their drive method.
print_status, which prints out the current information of each car as a clear, formatted table.
race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the
entire distance of the race.

Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is given a list of
ten cars similarly to the earlier exercise. The main program simulates the progressing of the race by calling the
hour_passes in a loop, after which it uses the race_finished method to check if the race has finished. The current
status is printed out using the print_status method every ten hours and then once more at the end of the race.'''

import random

class Car:

    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed):
        self.current_speed += speed

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def emergency_brake(self):
        self.accelerate(-200)

    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed

class Race:
    def __init__(self, race_name, race_length, number_of_cars):
        self.name = race_name
        self.length = race_length
        self.cars_in_the_race = number_of_cars
        self.cars = []
        for i in range(number_of_cars):
            self.cars.append(Car(f'ABC-{i}', random.randint(100, 200)))

    def full_race(self):
        j = 0
        while True:

            self.hour_passes()
            j +=1
            if j == 10:
                self.print_status()
                j = 0

            if self.race_finished():
                self.print_status()

                break

    def hour_passes(self):
        for i in range(len(self.cars)):
            self.cars[i].accelerate(random.randint(-10, 15))
            self.cars[i].drive(1)

    def print_status(self):
        print(f"{self.name} Registration Number  Travelled Distance  Current Speed  Max Speed")
        for car in self.cars:
            print(f'{"---":^{len(self.name)}}{car.registration_number :^19}  {car.travelled_distance :^18}  {car.current_speed:^13}{car.max_speed:^9}')

    def race_finished(self):
        for i in range(len(self.cars)):
            if self.cars[i].travelled_distance >= self.length:
                return True



race = Race('Grand Demolition Derby', 8000,11)

##race2 = Race('The Big Race',1000, 15)

race.full_race()

##race2.full_race()