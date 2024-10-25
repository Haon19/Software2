"""Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the
main program, create a list that consists of 10 car objects created using a loop. The maximum speed of each new car is
a random value between 100 km/h and 200 km/h. The registration numbers are created as follows: "ABC-1", "ABC-2" and so on.
Now the race begins. One per every hour of the race, the following operations are performed:

The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done
using the accerelate method.
Each car is made to drive for one hour. This is done with the drive method.

The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each car
are printed out formatted into a clear table."""

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



race_list = []

for i in range(10):
    car = Car(f'ABC-{i}', random.randint(100, 200))
    race_list.append(car)

racing = True
while racing:

    for car in race_list:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance > 10_000:
            racing = False

print("Registration Number  Travelled Distance  Current Speed  Max Speed")
for car in race_list:
    print(f'{car.registration_number :^19}  {car.travelled_distance :^18}  {car.current_speed:^13}{car.max_speed:^9}')