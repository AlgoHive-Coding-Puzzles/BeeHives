class Unveil:
    def __init__(self, lines: list):
        self.lines = lines
        
    def run(self):
        lines = [line for line in self.lines if 2000 <= int(line.strip()) <= 3000]
        lines = [line.strip() for line in lines]

        total = 0
        for i in range(len(lines)):
            # Impair et divisible par 3
            if not int(lines[i]) % 2 == 0 and int(lines[i]) % 3 == 0:
                total += int(lines[i])
                
        return total
    
if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    unveil = Unveil(lines)
    solution = unveil.run()
    print(solution)
    
    