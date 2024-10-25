'''Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor.
If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down
methods as many times as it needs to get to the fifth floor. The methods run the elevator one floor up or down and tell
what floor the elevator is after each move. Test the class by creating an elevator in the main program, tell it to move
to a floor of your choice and then back to the bottom floor.'''

class Elevator:
    def __init__(self,b_floor,t_floor):
        self.bottom_floor = b_floor
        self.top_floor = t_floor
        self.floor = self.bottom_floor

    def go_to_floor(self,floor):
        self.floor = floor
    def floor_up(self):
        self.floor = self.floor + 1
    def floor_down(self):
        self.floor = self.floor - 1

elevator = Elevator(0,10)

print(elevator.floor)

elevator.floor_up()

print(elevator.floor)

elevator.go_to_floor(5)

print(elevator.floor)

elevator.go_to_floor(elevator.top_floor)

print(elevator.floor)

elevator.go_to_floor(elevator.bottom_floor)

print(elevator.floor)