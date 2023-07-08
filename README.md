# Elevator Simulation

## Prerequisites

- Python installed on your machine

## Dependencies
List of python dependencies:
* argparse
* pytest

## Intro

This project is an elevator simulation that models the behavior of a single elevator that visits a list of different floors. It provides a flexible framework to simulate elevator operations, calculate travel times, and track visited floors.

## Assumptions

1. **Single Elevator:** Assume that the simulation involves a single elevator. If multiple elevators are required, the code would need to be extended to handle and manage multiple elevators simultaneously.

2. **Start Floor:** Assume that the elevator starts at a specific floor, which is provided via the first entry in the list of floors as input.

3. **Valid Floors Input:** Assume that the input list of floors to visit consists of valid floor numbers (integers) within the building's range.

4. **Floor Ordering:** Assume that the order of the floors in the input list represents the desired visitation order, and the elevator should follow that order.

5. **Travel Time Calculation:** Assume that the travel time between floors is calculated by multiplying the travel distance (number of floors) by a constant travel time per floor (10).

6. **Same Floor Visits:** Assume that visiting the same floor multiple times is valid.

7. **No Intermediate Stops:** Assume that the elevator goes directly to each floor in the input list without making any intermediate stops.

8. **Fastest Path:** Assume that the elevator has the potential to take the fastest path given a list of floors. This is an optional feature that is **disabled** by default.

## Features Not Included

1. **Multiple Elevators:** This simulation does not model multiple elevators that would run simultaneously. If multiple elevators are required, the code would need to be extended to handle and manage multiple elevators simultaneously.

2. **Real Time Updates:** This simulation does not model a real-world elevator in the sense of periodic updates or event-driven updates triggered by user input or external factors like floor requests or sensor data during the simulation.

## Setup

Follow these steps to set up the project:

1. Clone the repository:

    ```bash
    git clone https://github.com/Korysam15/elevator-simulation.git
    ```

2. Set up a virtual environment (optional, but recommended):
   
    a) Open a command line or terminal.
    
    b) Navigate to the desired location where you want to create the Python environment.
    
    c) Run the following command to create a virtual environment:
    
       - On Windows:

          python -m venv myenv

       - On macOS/Linux:

         python3 -m venv myenv

       Replace `myenv` with the desired name for your virtual environment.
    
    d) After the virtual environment is created, you need to activate it:

       - On Windows:

         myenv\Scripts\activate

       - On macOS/Linux:

         source myenv/bin/activate
    
       Once activated, your command prompt or terminal prompt should change to indicate that you are now in the virtual environment.

3. Install the required packages by running the following command:
   
    pip install -r requirements.txt

    This command will install the necessary packages specified in the `requirements.txt` file.

## Usage

To run the code via the Python command line, follow these steps:

1. Open a command line or terminal.

2. Navigate to the project directory.

3. Make sure you have activated the virtual environment (if you're using one).

4. Run the following command:

```bash
python main.py --floors 12 2 9 1 32
```

Replace the `--floors` argument with your desired list of floors to visit. You can provide multiple floor numbers separated by spaces.

5. The program will simulate the elevator's travel and display the total travel time and the floors visited in order.

Example output:

    Total travel time: 560
    Floors visited in order: [12, 2, 9, 1, 32]

6. You can try different floor combinations by changing the `--floors` argument and rerunning the command.

## Tests

To run the tests for this project using pytest, follow these steps:

1. Open a command line or terminal.

2. Navigate to the project directory.

3. Make sure you have activated the virtual environment (if you're using one).

4. Run the following command:

```bash
pytest tests
```

This command will automatically discover and execute all the test files in the project directory.

5. Wait for pytest to run the tests. It will provide detailed output indicating whether each test passed or failed.

6. After the tests have completed, pytest will display a summary of the test results, including the number of tests run and any failures or errors encountered.
