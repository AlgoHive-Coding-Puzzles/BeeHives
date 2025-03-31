import re

class Decrypt:
    def __init__(self, lines: list):
        self.lines = lines
        
    def run(self):
        possible = {'red': 12, 'green': 13, 'blue': 14}
        total = 0
        print(self.lines)
        for id, game in enumerate(self.lines, start=1):
            print(game)
            for n, color in re.findall(r'(\d+) (red|green|blue)', game):
                print(f"n: {n}, color: {color}")
                if possible[color] < int(n):
                    break
            else:
                total += id

        return total
    
if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    decrypt = Decrypt(lines)
    solution = decrypt.run()
    print(solution)
    
    