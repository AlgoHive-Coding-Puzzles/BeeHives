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
        unique_set = set()
        # Fill the set with values from 1 to 9999
        for i in range(1, 10000):
            unique_set.add(i)
            
        # Pick a random sample of unique values from the set
        for i in range(self.lines_count):
            # Take a random  value from the set
            line = random.choice(list(unique_set))
            lines.append(str(line))
            # Remove the value from the set to ensure uniqueness
            unique_set.remove(line)
            
        return lines
        
        
    
if __name__ == '__main__':
    lines_count = int(sys.argv[1])
    unique_id = sys.argv[2]
    forge = Forge(lines_count, unique_id)
    lines = forge.run()
    with open('input.txt', 'w') as f:
        f.write('\n'.join(lines) + '\n')
