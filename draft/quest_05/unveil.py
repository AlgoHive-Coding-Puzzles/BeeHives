import re
import math

class Unveil:
    def __init__(self, lines: list):
        self.lines = lines
        
    def run(self):
        total = 0
        for game in self.lines:
            max_number = {'red': 0, 'green': 0, 'blue': 0}
            for n, color in re.findall(r'(\d+) (red|green|blue)', game):
                max_number[color] = max(int(n), max_number[color])

            total += math.prod(max_number.values())

        return total
    
if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    unveil = Unveil(lines)
    solution = unveil.run()
    print(solution)