"""Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled
distance. Add a class initializer that sets the first two of the properties based on parameter values. The current speed
and travelled distance of a new car must be automatically set to zero. Write a main program where you create a new car
(registration number ABC-123, maximum speed 142 km/h). Finally, print out all the properties of the new car."""

class Car:

    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = Car(registration_number="ABC-123", max_speed=142)

print(car.registration_number)
print(car.max_speed)
print(car.current_speed)
print(car.travelled_distance)
