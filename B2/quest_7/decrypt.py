class Decrypt:
    def __init__(self, lines: list):
        self.lines = lines

    def run(self):
        # For the first part, we'll only find words horizontally and vertically
        found_words = []
        
        # Parse the grid
        self.grid = []
        for line in self.lines:
            if isinstance(line, str):
                self.grid.append(line.strip())
            else:
                self.grid.append(line)
        
        # Search horizontally
        for i in range(len(self.grid)):
            for word in ["python", "algorithm", "puzzle", "coding", "search"]:
                row = self.grid[i]
                if word in row:
                    found_words.append((word, i + 1, row.index(word) + 1, "right"))
                # Also check reversed
                rev_word = word[::-1]
                if rev_word in row:
                    found_words.append((rev_word, i + 1, row.index(rev_word) + 1, "left"))
        
        # Search vertically
        for j in range(len(self.grid[0]) if self.grid else 0):
            col = ''.join(self.grid[i][j] for i in range(len(self.grid)) if j < len(self.grid[i]))
            for word in ["python", "algorithm", "puzzle", "coding", "search"]:
                if word in col:
                    found_words.append((word, col.index(word) + 1, j + 1, "down"))
                # Also check reversed
                rev_word = word[::-1]
                if rev_word in col:
                    found_words.append((rev_word, col.index(rev_word) + 1, j + 1, "up"))
        
        return len(found_words)

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    decrypt = Decrypt(lines)
    solution = decrypt.run()
    print(solution)