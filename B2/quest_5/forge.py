# forge.py - Génère input.txt
import sys
import random

class Forge:
    def __init__(self, lines_count: int, unique_id: str = None):
        self.lines_count = lines_count
        self.unique_id = unique_id
    
    def run(self) -> list:
        random.seed(self.unique_id)
        # Generate random numbers for the list
        numbers = random.sample(range(1, 100), self.lines_count - 1)  # Generate n-1 random numbers
        # Generate a target
        target = random.randint(10, 100)
        
        # Ensure at least one pair exists that sums to the target
        # Add a valid pair (x, y) where x + y = target
        x = random.randint(1, target // 2)
        y = target - x
        numbers.append(x)
        numbers.append(y)
        
        # Shuffle the numbers to make it appear random
        random.shuffle(numbers)
        
        lines = ["Objectif : " + str(target)]
        lines.append(map(str, numbers))
        
        return lines
    
    def generate_line(self) -> str:
        return str(random.randint(1, 100))

if __name__ == '__main__':
    lines_count = int(sys.argv[1])
    unique_id = sys.argv[2]
    forge = Forge(lines_count, unique_id)
    numbers, target = forge.run()
    with open('input.txt', 'w') as f:
        f.write(' '.join(map(str, numbers)) + '\n')
        f.write(str(target) + '\n')
