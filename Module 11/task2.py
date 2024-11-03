"""Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar. Electric cars have the
capacity of the battery in kilowatt-hours as their property. Gasoline cars have the volume of the tank in liters as
their property. Write initializers for the subclasses. For example, the initializer of electric cars receives the
registration number, maximum speed and battery capacity as its parameter. It calls the initializer of the base class to
set the first two properties and then sets its capacity. Write a main program where you create one electric car
(ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars, make them
drive for three hours and print out the values of their kilometer counters."""

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

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed,tank_capacity):
        self.capacity = tank_capacity
        super().__init__(registration_number, max_speed)

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery):
        self.battery = battery
        super().__init__(registration_number, max_speed)

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


e_car = ElectricCar('ABC-15', 180, 52.5)

ice_car = GasolineCar('ACD-123', 165, 32.3)

e_car.accelerate(100)
ice_car.accelerate(120)

for i in range(3):
    e_car.drive(1)
    ice_car.drive(1)

print(e_car.travelled_distance)
print(ice_car.travelled_distance)