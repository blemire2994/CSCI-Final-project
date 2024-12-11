from collections import deque
from heapq import heappop, heappush
from output import format_steps, print_path_on_maze  # Import utilities

def is_valid_move(maze, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(maze, start, end, print_steps=True):
    open_list = []
    heappush(open_list, (0 + heuristic(start, end), 0, start))  # (f_score, g_score, position)

    came_from = {}  # To reconstruct the path
    g_score = {start: 0}
    steps = []  # Track steps

    while open_list:
        _, current_g, current = heappop(open_list)
        steps.append(current)  # Record the step

        if current == end:
            if print_steps:
                print("Steps taken in A* (Formatted):")
                print(format_steps(steps))  # Use the formatted output
                print("\nPath in the Maze:")
                print_path_on_maze(maze, steps)  # Use the grid output
            return True  # Path found, return True

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if not is_valid_move(maze, neighbor[0], neighbor[1]):
                continue

            tentative_g_score = current_g + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, end)
                heappush(open_list, (f_score, tentative_g_score, neighbor))
                came_from[neighbor] = current

    if print_steps:
        print("Steps taken in A* (Formatted):")
        print(format_steps(steps))  # Use the formatted output
        print("\nNo path found in the Maze.")
    return False  # Path not found


def bfs(maze, start, end,print_steps=True):
    queue = deque([(start[0], start[1])])
    visited = set()
    visited.add(start)
    steps = []

    while queue:
        x, y = queue.popleft()
        steps.append((x, y))

        if (x, y) == end:
            if print_steps:
                print("Steps taken in BFS (Formatted):")
                print(format_steps(steps))  # Use formatted output
                print("\nPath in the Maze:")
                print_path_on_maze(maze, steps)  # Use grid output
            return True

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(maze, new_x, new_y) and (new_x, new_y) not in visited:
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))


    if print_steps:
        print("Steps taken in BFS (Formatted):")
        print(format_steps(steps))  # Use formatted output
        print("\nNo path found in the Maze.")
    return False

def dfs(maze, x, y, visited, print_steps=True, steps=None, end=None):
    if steps is None:
        steps = []  # Initialize the steps list if not provided

    steps.append((x, y))  # Record the current step


    if (x, y) == end:
        if print_steps:
            print("Steps taken in DFS (Formatted):")
            print(format_steps(steps))  # Use formatted output
            print("\nPath in the Maze:")
            print_path_on_maze(maze, steps)  # Use grid output
        return True

    visited.add((x, y))

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(maze, new_x, new_y) and (new_x, new_y) not in visited:
            if dfs(maze, new_x, new_y, visited, print_steps, steps, end):
                return True

    steps.pop()  # Remove the current step if it leads to a dead end
    return False

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

start = (7, 1)
end = (1, 5)


print("BFS with steps:")
print("\nBFS Result:", bfs(maze, start, end, print_steps=True))


print("\nDFS with steps:")
dfs_result = dfs(maze, start[0], start[1], set(), print_steps=True, end=end)
print("DFS Result:", dfs_result)

print("\nA* with steps:")
a_star_result = a_star_search(maze, start, end, print_steps=True)
print("A* Result:", a_star_result)
