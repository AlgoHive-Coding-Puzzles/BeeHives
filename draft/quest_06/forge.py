# forge.py - Génère input.txt
import sys
import random

class Forge:
    def __init__(self, lines_count: int, unique_id: str = None):
        self.lines_count = lines_count
        self.unique_id = unique_id
    
    def run(self) -> list:
        random.seed(self.unique_id)
        # Generate a target
        target = random.randint(10, 100)
        
        lines = []
        
        generate_valid_answers_count = random.randint(1, self.lines_count // 2)
        for _ in range(generate_valid_answers_count):
            # Generate a valid answer
            x = random.randint(1, target)
            y = target - x
            line = "(" + str(x) + ", " + str(y) + ")"
            lines.append(line)
        
        # Generate invalid answers
        generate_invalid_answers_count = self.lines_count - generate_valid_answers_count
        for _ in range(generate_invalid_answers_count):
            # Generate an invalid answer
            lines.append(self.generate_line())

        # Shuffle the lines to mix valid and invalid answers
        random.shuffle(lines)
        
        # Add the objective line at the very beginning
        lines.insert(0, "Objectif: " + str(target))
        
        return lines
    
    def generate_line(self) -> str:
        return str("(" + str(random.randint(1, 100)) + ", " + str(random.randint(1, 100)) + ")")

if __name__ == '__main__':
    lines_count = int(sys.argv[1])
    unique_id = sys.argv[2]
    forge = Forge(lines_count, unique_id)
    lines = forge.run()
    with open('input.txt', 'w') as f:
        f.write('\n'.join(lines) + '\n')

