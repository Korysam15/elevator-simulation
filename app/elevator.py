class Elevator:
    # Constant travel time for a single floor
    TRAVEL_TIME = 10
    
    # Constructor (start_floor = number)
    def __init__(self, floors_to_visit):
        if not floors_to_visit:
            raise Exception("Array is empty!")
        self.current_floor, *self.floors_to_visit = floors_to_visit
        self.total_travel_time = 0
        self.visited_floors = [self.current_floor]

    # Add floor to list of floors to visit
    def add_floor_to_visit(self, floor):
        self.floors_to_visit.append(floor)

    # Kick off floor visitation for elevator
    def visit_floors(self, take_fastest_path=False):
        if not self.floors_to_visit:
            return self.total_travel_time, self.visited_floors

        self.floors_to_visit = sorted(self.floors_to_visit) if take_fastest_path else self.floors_to_visit

        for floor in self.floors_to_visit:
            travel_distance = abs(self.current_floor - floor)
            travel_time = travel_distance * self.TRAVEL_TIME
            self.total_travel_time += travel_time

            self.current_floor = floor
            self.visited_floors.append(self.current_floor)

        return self.total_travel_time, self.visited_floors