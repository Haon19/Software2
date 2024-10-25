"""Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5)
increases the travelled distance to 2090 km."""

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

car = Car(registration_number="ABC-123", max_speed=142)

car.accelerate(30)

car.drive(1.5)

car.accelerate(70)

car.drive(1.5)

car.accelerate(50)

car.drive(1.5)

print(car.current_speed)

car.emergency_brake()

print(car.registration_number)
print(car.max_speed)
print(car.current_speed)
print(car.travelled_distance)