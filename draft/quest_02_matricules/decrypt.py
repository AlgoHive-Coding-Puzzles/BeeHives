class Decrypt:
    def __init__(self, lines: list):
        self.lines = lines
        
    def run(self):
        lines = [line for line in self.lines if 3000 <= int(line.strip()) <= 4000]
        lines = [line.strip() for line in lines]

        total = 0
        for i in range(len(lines)):
            matricule_sum = sum(int(digit) for digit in lines[i])
            if matricule_sum >= 20:
                total += matricule_sum
                
        return total
        
    
if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    decrypt = Decrypt(lines)
    solution = decrypt.run()
    print(solution)
    
    