import sys
import random

class Forge:
    def __init__(self, lines_count: int, unique_id: str = None):
        self.lines_count = 30
        self.unique_id = unique_id
    
    def run(self) -> list:
        """
        Generate a grid with ., R, O, and a single cross (starting points) and then a bunch of movements.
        """
        random.seed(self.unique_id)
        grid = []
        
        # Generate the grid with random characters
        for _ in range(self.lines_count):
            row = [random.choice(['.', '.', '.', 'R', 'R', 'R', 'R', 'O']) for _ in range(self.lines_count)]
            grid.append(row)
        
        # Place a single cross ('X') randomly in the grid
        x, y = random.randint(0, self.lines_count - 1), random.randint(0, self.lines_count - 1)
        grid[x][y] = 'X'
        
        # Convert grid rows to strings
        grid_lines = [' '.join(row) for row in grid]
        
        # Generate random movements Mouvements : SE, SE, N, NW
        movements_text = "Mouvements : "
        movements = []
        
        # Movements are random directions in a hexagonal grid, but must stays within the grid, starting from the cross
        directions = ['N', 'NE', 'SE', 'S', 'SW', 'NW']
        for _ in range(15):
            # Ensure the movement stays within the grid
            direction = random.choice(directions)
            if direction == 'N' and x > 0:
                x -= 1
            elif direction == 'NE' and x > 0 and y < self.lines_count - 1:
                x -= 1
                y += 1
            elif direction == 'SE' and x < self.lines_count - 1 and y < self.lines_count - 1:
                x += 1
                y += 1
            elif direction == 'S' and x < self.lines_count - 1:
                x += 1
            elif direction == 'SW' and x < self.lines_count - 1 and y > 0:
                x += 1
                y -= 1
            elif direction == 'NW' and x > 0 and y > 0:
                x -= 1
                y -= 1
            movements.append(direction)
        
        movements = movements_text + ', '.join(movements)
        
        # Combine grid and movements
        return grid_lines + [movements]

if __name__ == '__main__':
    lines_count = int(sys.argv[1])
    unique_id = sys.argv[2]
    forge = Forge(lines_count, unique_id)
    lines = forge.run()
    with open('input.txt', 'w') as f:
        f.write('\n'.join(lines) + '\n')
