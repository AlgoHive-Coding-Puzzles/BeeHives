import time
import os

class Unveil:
    def __init__(self, lines: list):
        self.lines = lines

    def run(self):
        # Parse the grid
        grid = [line.split() for line in self.lines[:-1]]

        # Find the starting position ('X')
        start_x, start_y = None, None
        for i, row in enumerate(grid):
            if 'X' in row:
                start_x, start_y = row.index('X'), i
                break
        
        def generate_spiral(length):
                spiral = ["NE"]
                spiral += ["SE"] * (length - 1)
                spiral += ["S"] * (length)
                spiral += ["SW"] * (length)
                spiral += ["NW"] * (length)
                spiral += ["N"] * (length)
                spiral += ["NE"] * (length)
                # print(spiral)
                return spiral
            
        # (x, y)
        direction_map = {
            "N": (0, -1),
            "NE": (1, -1),
            "NW": (-1, -1),
            "S": (0, 1),
            "SE": (1, 1),
            "SW": (-1, 1),
        }

        # Helper to check if a cell is within bounds
        def is_valid(y, x):
            return 0 <= y < len(grid) and 0 <= x < len(grid[0])

        # Perform the spiral traversal
        visited = set()
        path = []
        score = 0
        x, y = start_x, start_y
        visited.add((y, x))
        path.append((y, x))

        def display_grid():
            os.system('clear')  # Clear the console
            for i, row in enumerate(grid):
                for j, cell in enumerate(row):
                    if (i, j) in visited:
                        print(f"\033[92m{cell}\033[0m", end=" ")  # Highlight visited cells in green
                    else:
                        print(cell, end=" ")
                print()
            print(f"\nCurrent Score: {score}")
            print(f"Current Path: {path}")
            time.sleep(0.3)

        # Spiral logic
        spiral_length = 1
        path_length = 0
        direction_index = 0  # Track the current direction index
        while True:
            moved = False
            directions = generate_spiral(spiral_length)
            for _ in range(len(directions)):
                direction = directions[direction_index]
                direction_index = (direction_index + 1) % len(directions)
                dx, dy = direction_map[direction]
                if is_valid(y + dy, x + dx):
                    y += dy
                    x += dx
                    visited.add((y, x))
                    path.append((y, x))
                    cell = grid[y][x]
                    # print(f"{direction} : ({x}, {y}) = {cell}")
                    if cell == ".":
                        score += 0
                    elif cell == "R":
                        score += 5
                    elif cell == "O":
                        score -= 1
                    moved = True
                    path_length += 1
                    # display_grid()
                else:
                    break
            if not moved:
                break
            else:
                spiral_length += 1

        return path_length * score

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    unveil = Unveil(lines)
    score = unveil.run()
    print(score)

