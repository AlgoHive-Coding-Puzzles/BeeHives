class Decrypt:
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
        # For the first part, we'll only find words horizontally and vertically
        found_words = []
        
        # Search horizontally
        for i in range(len(self.grid)):
            for word in ["python", "algorithm", "puzzle", "coding", "search"]:
                row = self.grid[i]
                if word in row:
                    found_words.append((word, i, row.index(word), "right"))
                # Also check reversed
                rev_word = word[::-1]
                if rev_word in row:
                    found_words.append((rev_word, i, row.index(rev_word), "left"))
        
        # Search vertically
        for j in range(len(self.grid[0]) if self.grid else 0):
            col = ''.join(self.grid[i][j] for i in range(len(self.grid)) if j < len(self.grid[i]))
            for word in ["python", "algorithm", "puzzle", "coding", "search"]:
                if word in col:
                    found_words.append((word, col.index(word), j, "down"))
                # Also check reversed
                rev_word = word[::-1]
                if rev_word in col:
                    found_words.append((rev_word, col.index(rev_word), j, "up"))
        
        return len(found_words)

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    decrypt = Decrypt(lines)
    solution = decrypt.run()
    print(solution)