
# Maze Solver User Documentation

## Overview

This project is a Python-based implementation of three popular pathfinding algorithms: **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **A𝑥 (A-star) Search**. It allows users to find a path from a given start point to an end point within a maze. This documentation will guide you through the project's structure, usage instructions, and customization options.

---

## Features
- **Algorithms**: BFS, DFS, and A𝑥 (A-star) Search.
- **Visualization**: Outputs the maze with the discovered path.
- **Formatted Output**: Displays the steps taken to solve the maze in a human-readable format.
- **Customizable**: Easily adapt the maze and starting/ending points.

---

## Project Structure

### Files
1. **`final.py`**
   - Contains the implementation of BFS, DFS, and A𝑥 Search algorithms.
   - Includes utility functions to validate moves and calculate heuristics.

2. **`output.py`**
   - Contains utility functions for formatting and visualizing the path:
     - `format_steps`: Formats the steps as a string.
     - `print_path_on_maze`: Prints the maze with the path indicated by `*`.

---

## Getting Started

### Prerequisites
- Python 3.7 or higher

### Installation
1. Clone or download the repository.
2. Ensure the required files (`final.py`, `output.py`) are in the same directory.

### Running the Program
1. Open a terminal or command prompt.
2. Navigate to the directory containing the files.
3. Run the program using the following command:

   ```bash
   python final.py
   ```

### Example Output
The program uses a sample maze and outputs the steps and path for each algorithm.

#### Sample Maze
```plaintext
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 1 1 0 1
1 1 1 1 1 0 1 1 0 1
1 0 0 0 1 0 0 0 0 1
1 0 1 0 1 1 1 1 0 1
1 0 1 0 0 0 0 1 0 1
1 0 1 1 1 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
```

#### Algorithms Output
- **BFS**:
  ```plaintext
  Steps taken in BFS (Formatted):
  (7,1) → (7,2) → (7,3) → ... → (1,5)

  Path in the Maze:
  1 1 1 1 1 1 1 1 1 1
  1 0 0 0 0 * 1 1 0 1
  1 1 1 1 1 * 1 1 0 1
  1 0 0 0 1 * * * * 1
  ...
  ```

- **DFS**:
  Similar format but may show a different path.

- **A\* Search**:
  Similar format but optimized based on the heuristic.

---

## Customization

### Modifying the Maze
The maze is defined in `final.py` as a 2D list:
```python
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    ...
]
```
- `1` represents walls.
- `0` represents open paths.

### Changing Start and End Points
The start and end points are defined in `final.py`:
```python
start = (7, 1)
end = (1, 5)
```

---

## Troubleshooting

### Common Issues
1. **Incorrect Maze Format**:
   Ensure the maze is a rectangular grid and all rows have the same length.

2. **Unreachable End Point**:
   Verify that a path exists between the start and end points.

3. **Python Version Compatibility**:
   Use Python 3.7 or higher.

---

## Contact
For questions or contributions, feel free to reach out to David Capobianco, Brett Lemire, or Christopher DiGioia.
