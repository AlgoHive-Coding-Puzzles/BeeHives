class Decrypt:
    def __init__(self, lines: list):
        self.lines = lines

    def run(self):
        target = int(self.lines[0].split(": ")[1])
        # each lines looks like "(x, y)"
        
        result = []
        for line in self.lines[1:]:
            x, y = line.strip()[1:-1].split(", ")
            if int(x) + int(y) == target:
                result.append((x, y))
                    
        return len(result)
        

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    decrypt = Decrypt(lines)
    solution = decrypt.run()
    print(solution)
