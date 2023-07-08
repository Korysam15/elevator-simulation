import argparse
import lib
import sys
from elevator import Elevator

# Kicks off elevators to visit floors
def run(elevators):
    total_travel_times = []
    visited_floors_list = []

    for elevator in elevators:
        total_travel_time, visited_floors = elevator.visit_floors()
        total_travel_times.append(total_travel_time)
        visited_floors_list.append(visited_floors)
    
    return total_travel_times, visited_floors_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    parser.add_argument('--floors', type=lib.list2i, help="A list of floors the elevator should visit. Index [0]=starting floor")
    args = parser.parse_args()

    floors_to_visit=args.floors

    elevator = Elevator(floors_to_visit=floors_to_visit)

    elevators = [elevator]
    
    total_travel_times, visited_floors_list = run(elevators)

    for i, elevator in enumerate(elevators):
        print("Total travel time:", total_travel_times[i])
        print("Floors visited in order:", visited_floors_list[i])
        print()