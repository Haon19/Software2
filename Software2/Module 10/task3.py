'''Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators
to the bottom floor. Continue the main program by causing a fire alarm in your building.'''


class Elevator:
    def __init__(self,b_floor,t_floor):
        self.bottom_floor = b_floor
        self.top_floor = t_floor
        self.floor = self.bottom_floor

    def go_to_floor(self,floor):
        self.floor = floor

        if self.floor < self.bottom_floor:
            self.floor = self.bottom_floor

        elif self.floor > self.top_floor:
            self.floor = self.top_floor

    def floor_up(self):
        self.floor = self.floor + 1

        if self.floor < self.bottom_floor:
            self.floor = self.bottom_floor

        elif self.floor > self.top_floor:
            self.floor = self.top_floor

    def floor_down(self):
        self.floor = self.floor - 1

        if self.floor < self.bottom_floor:
            self.floor = self.bottom_floor

        elif self.floor > self.top_floor:
            self.floor = self.top_floor

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

    def fire_alarm(self):
        for i in range(self.number_of_elevators):
            self.elevator_list[i].go_to_floor(self.bottom_floor)


elevator = Elevator(0,10)

building = Building(0,10,5)

for i in range(building.number_of_elevators):
    print(building.elevator_list[i].floor)

building.run_elevators(5)

for i in range(building.number_of_elevators):
    print(building.elevator_list[i].floor)

building.fire_alarm()

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