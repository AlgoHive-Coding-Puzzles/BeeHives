# forge.py - Génère input.txt
import sys
import random

class Forge:
    def __init__(self, lines_count: int, unique_id: str = None):
        self.lines_count = lines_count
        self.unique_id = unique_id
    
    def run(self) -> list:
        random.seed(self.unique_id)
        lines = []
        for _ in range(250):
            lines.append(self.generate_line(_))
        return lines
    
    def generate_line(self, index: int) -> str:
        # Pick a random number between 2 and 7 (inclusive)
        subset_count = random.randint(2, 5)
        subsets = [self.generate_subset() for _ in range(subset_count) ]
        return f"Round {index + 1}: {'; '.join(subsets)}"
        
    def generate_subset(self) -> str:
        colors = ['green', 'blue', 'red']
        counts = [random.randint(0, 20) for _ in range(3)]
        subset = []
        for color, count in zip(colors, counts):
            if count > 0:
                subset.append(f"{count} {color}")
        random.shuffle(subset)
        return ', '.join(subset)

if __name__ == '__main__':
    lines_count = int(sys.argv[1])
    unique_id = sys.argv[2]
    forge = Forge(lines_count, unique_id)
    lines = forge.run()
    with open('input.txt', 'w') as f:
        f.write('\n'.join(lines))