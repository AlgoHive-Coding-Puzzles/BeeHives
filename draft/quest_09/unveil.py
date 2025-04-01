import math
from heapq import heappush, heappop

class Unveil:
    def __init__(self, lines: list):
        self.lines = lines
        
    def run(self):
        grid = [list(int(y) for y in list(x.strip())) for x in self.lines]
        
        def add(queue, heat_loss: int, row: int, col: int, dr: int, dc: int, steps: int = 1):
            new_row = row + dr
            new_col = col + dc

            if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row])):
                return

            heappush(
                queue,
                (
                    heat_loss + grid[new_row][new_col],
                    new_row,
                    new_col,
                    dr,
                    dc,
                    steps,
                ),
            )
            
        visited = set()
        priority_queue = [(0, 0, 0, 0, 0, 0)]
        
        while priority_queue:
            heat_loss, row, col, dr, dc, steps = heappop(priority_queue)

            if steps >= 4 and row == len(grid) - 1 and col == len(grid[row]) - 1:
                break

            if (row, col, dr, dc, steps) in visited:
                continue

            visited.add((row, col, dr, dc, steps))

            if steps < 6 and (dr, dc) != (0, 0):
                add(priority_queue, heat_loss, row, col, dr, dc, steps + 1)

            if steps >= 4 or (dr, dc) == (0, 0):
                for new_dr, new_dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if (new_dr, new_dc) != (dr, dc) and (new_dr, new_dc) != (-dr, -dc):
                        add(priority_queue, heat_loss, row, col, new_dr, new_dc)
                  
        return heat_loss
    
if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    unveil = Unveil(lines)
    solution = unveil.run()
    print(solution)
    
    