import pytest
from app.elevator import Elevator

def test_visit_floors_without_take_fastest_path():
    elevator = Elevator([12, 2, 9, 1, 32])
    total_travel_time, visited_floors = elevator.visit_floors()
    assert total_travel_time == 560
    assert visited_floors == [12, 2, 9, 1, 32]

def test_visit_floors_with_take_fastest_path():
    elevator = Elevator([12, 2, 9, 1, 32])
    total_travel_time, visited_floors = elevator.visit_floors(take_fastest_path=True)
    assert total_travel_time == 420
    assert visited_floors == [12, 1, 2, 9, 32]

def test_visit_floors_negative():
    elevator = Elevator([0, -5, -10, 0, 10])
    total_travel_time, visited_floors = elevator.visit_floors()
    assert total_travel_time == 300
    assert visited_floors == [0, -5, -10, 0, 10]

def test_visit_floors_empty():
    with pytest.raises(Exception, match="Array is empty!"):
        elevator = Elevator([])

def test_visit_floors_single_floor():
    elevator = Elevator([10])
    total_travel_time, visited_floors = elevator.visit_floors()
    assert total_travel_time == 0
    assert visited_floors == [10]

def test_visit_floors_same_floor():
    elevator = Elevator([5, 5, 5, 5])
    total_travel_time, visited_floors = elevator.visit_floors()
    assert total_travel_time == 0
    assert visited_floors == [5, 5, 5, 5]

def test_add_floor_to_visit():
    elevator = Elevator([10, 20, 30])
    elevator.add_floor_to_visit(15)
    total_travel_time, visited_floors = elevator.visit_floors()
    assert total_travel_time == 350
    assert visited_floors == [10, 20, 30, 15]