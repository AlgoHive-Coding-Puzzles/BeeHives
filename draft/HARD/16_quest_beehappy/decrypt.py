class Decrypt:
    def __init__(self, lines: list):
        self.lines = lines
        
    def run(self):
        # Strip the lines
        self.lines = [line.strip() for line in self.lines]
        # Count the amount of 🐝
        count = 0
        for line in self.lines:
            count += line.count('🐝')
            
        return count
    
if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    decrypt = Decrypt(lines)
    solution = decrypt.run()
    print(solution)
    
    