# Maze Generator and Solver

This project generates, displays, and solves a random maze.

## Features

- **Maze Generation:** Generates random mazes using a recursive backtracker algorithm.
- **Visualization:** Provides a visual representation of the maze.

## Usage

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/JacobA12/maze_solver.git
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd maze_solver
    ```

3.  **Run the program:**

    ```bash
    ./main.sh
    ```

## Dependencies

- Python 3.x
- tkinter

## Algorithm

The maze is generated using a recursive backtracker algorithm, implemented in the [`Maze._break_walls_r`](src/maze.py) method of the [src/maze.py](src/maze.py) file.

## Testing

To run the tests, execute:

```bash
./test.sh
```

## Credit

I created this application following the Boot.dev course.

https://github.com/bootdotdev/curriculum
