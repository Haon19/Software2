'''Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers
of the bottom and top floors and the number of elevators in the building. When a building is created, the building
creates the required number of elevators. The list of elevators is stored as a property of the building. Write a method
called run_elevator that accepts the number of the elevator and the destination floor as its parameters. In the main
program, write the statements for creating a new building and running the elevators of the building.'''

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

class Building:
    def __init__(self,b_floor,t_floor,num_of_elevators):
        self.bottom_floor = b_floor
        self.top_floor = t_floor
        self.number_of_elevators = num_of_elevators
        self.elevator_list = []

        for i in range(num_of_elevators):
            self.elevator_list.append(Elevator(b_floor,t_floor))

    def run_elevators(self, dest_floor):
        for i in range(self.number_of_elevators):
            self.elevator_list[i].go_to_floor(dest_floor)


elevator = Elevator(0,10)

building = Building(0,10,5)

for i in range(building.number_of_elevators):
    print(building.elevator_list[i].floor)

building.run_elevators(100)

for i in range(building.number_of_elevators):
    print(building.elevator_list[i].floor)

print(elevator.floor)

elevator.floor_up()

print(elevator.floor)

elevator.go_to_floor(5)

print(elevator.floor)

elevator.go_to_floor(elevator.top_floor)

print(elevator.floor)

elevator.go_to_floor(elevator.bottom_floor)

print(elevator.floor)