class Unveil:
    def __init__(self, lines: list):
        self.lines = lines
        
    def run(self):
        return sum(int(num.strip()) if i % 2 == 0 else -int(num.strip()) for i, num in enumerate(self.lines))
    
if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    unveil = Unveil(lines)
    solution = unveil.run()
    print(solution)
    
    