# forge.py - Génère input.txt
import sys
import random
import string

class Forge:
    def __init__(self, lines_count: int, unique_id: str = None):
        self.lines_count = lines_count
        self.unique_id = unique_id
    
    def run(self) -> list:
        random.seed(self.unique_id)
        # Generate a grid of characters with hidden words
        grid_size = min(max(50, self.lines_count), 50)  # Grid size between 30 and 30
        grid = []
        
        # Generate the grid filled with random characters
        for i in range(grid_size):
            row = ''.join(random.choices(string.ascii_lowercase, k=grid_size))
            grid.append(row)
            
        # Choose words to hide in the grid
        words_to_hide = ['python', 'algorithm', 'puzzle', 'coding', 'search']
        hidden_words = []
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # right, down, diagonal down-right, diagonal down-left
        
        # the count of word we want to hide
        words_to_hide_count = random.randint(1, 50)
        # Try to place each word in the grid
        for i in range(words_to_hide_count):
            # Randomly select a word to hide
            word = random.choice(words_to_hide)
                
            # Try multiple times to place the word
            for attempt in range(50):
                direction = random.choice(directions)
                dx, dy = direction
                
                # Choose a starting position
                start_x = random.randint(0, grid_size - 1)
                start_y = random.randint(0, grid_size - 1)
                
                # Check if the word fits from this position
                if (0 <= start_x + (len(word)-1)*dx < grid_size and 
                    0 <= start_y + (len(word)-1)*dy < grid_size):
                    
                    # Create a modified grid to check placement
                    temp_grid = [list(row) for row in grid]
                    can_place = True
                    
                    # Check if the word can be placed
                    for i in range(len(word)):
                        x = start_x + i*dx
                        y = start_y + i*dy
                        if temp_grid[x][y] != word[i] and temp_grid[x][y] != grid[x][y]:
                            can_place = False
                            break
                    
                    if can_place:
                        # Place the word
                        for i in range(len(word)):
                            x = start_x + i*dx
                            y = start_y + i*dy
                            temp_grid[x][y] = word[i]
                        
                        # Update the grid
                        grid = [''.join(row) for row in temp_grid]
                        hidden_words.append((word, start_x, start_y, "right" if dx == 0 else "down" if dy == 0 else "diagonal"))
                        break
        
        return grid
    
    def generate_line(self, index: int) -> str:
        return str(random.randint(0, 100))

if __name__ == '__main__':
    lines_count = int(sys.argv[1])
    unique_id = sys.argv[2]
    forge = Forge(lines_count, unique_id)
    lines = forge.run()
    with open('input.txt', 'w') as f:
        f.write('\n'.join(lines) + '\n')
