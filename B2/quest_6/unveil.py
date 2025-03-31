class Unveil:
    def __init__(self, lines: list):
        self.lines = [line.strip() if isinstance(line, str) else line for line in lines]
        self.parse_input()
        
    def parse_input(self):
        # Parse the grid size
        self.grid_size = int(self.lines[0])
        
        # Parse the grid
        self.grid = []
        for i in range(1, self.grid_size + 1):
            if i < len(self.lines):
                self.grid.append(self.lines[i])
        
        # Parse number of hidden words
        if self.grid_size + 1 < len(self.lines):
            self.num_hidden_words = int(self.lines[self.grid_size + 1])
        else:
            self.num_hidden_words = 0
        
        # Parse hidden words
        self.hidden_words = []
        for i in range(self.grid_size + 2, min(self.grid_size + 2 + self.num_hidden_words, len(self.lines))):
            parts = self.lines[i].split()
            if len(parts) >= 4:
                self.hidden_words.append((parts[0], int(parts[1]), int(parts[2]), parts[3]))
    
    def run(self):
        # For the second part, we'll find words in all directions including diagonals
        found_words = []
        directions = [
            (0, 1, "right"),   # right
            (1, 0, "down"),    # down
            (0, -1, "left"),   # left
            (-1, 0, "up"),     # up
            (1, 1, "down-right"),    # diagonal down-right
            (1, -1, "down-left"),    # diagonal down-left
            (-1, 1, "up-right"),     # diagonal up-right
            (-1, -1, "up-left")      # diagonal up-left
        ]
        
        words_to_find = ["python", "algorithm", "puzzle", "coding", "search"]
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i]) if i < len(self.grid) else 0):
                for dx, dy, direction in directions:
                    for word in words_to_find:
                        # Check if the word fits from this position in this direction
                        if (0 <= i + (len(word)-1)*dx < len(self.grid) and 
                            all(0 <= j + k*dy < len(self.grid[i+k*dx]) if i+k*dx < len(self.grid) else False 
                                for k in range(len(word)))):
                            
                            # Check if the word matches
                            match = True
                            for k in range(len(word)):
                                x = i + k*dx
                                y = j + k*dy
                                if x >= len(self.grid) or y >= len(self.grid[x]) or self.grid[x][y] != word[k]:
                                    match = False
                                    break
                            
                            if match:
                                found_words.append((word, i, j, direction))
        
        # Calculate a score based on the words found
        score = 0
        for word, _, _, _ in found_words:
            score += len(word) * 10
        
        return score

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    unveil = Unveil(lines)
    solution = unveil.run()
    print(solution)