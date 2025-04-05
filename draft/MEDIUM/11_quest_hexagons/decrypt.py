class Decrypt:
    def __init__(self, lines: list):
        self.lines = lines

    def run(self):
        # Parse the grid and movements
        grid = [line.split() for line in self.lines[:-1]]
        movements_line = self.lines[-1].strip()
        movements = movements_line.split(":")[1].strip().split(", ")
        print(movements)

        # Find the starting position ('X')
        start_x, start_y = None, None
        for i, row in enumerate(grid):
            if 'X' in row:
                start_x, start_y = row.index('X'), i
                break

        # Define the movement directions
        directions = {
            "N": (0, -1),
            "NE": (1, -1),
            "NW": (-1, -1),
            "S": (0, 1),
            "SE": (1, 1),
            "SW": (-1, 1),
        }

        # Calculate the total score
        score = 0
        x, y = start_x, start_y
        for move in movements:
            dx, dy = directions[move]
            x += dx
            y += dy
            cell = grid[y][x]
            if cell == ".":
                score += 0
            elif cell == "R":
                score += 5
            elif cell == "O":
                score -= 1
                
        return score

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    decrypt = Decrypt(lines)
    solution = decrypt.run()
    print(solution)

