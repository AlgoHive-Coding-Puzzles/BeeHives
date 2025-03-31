class Decrypt:
    def __init__(self, lines: list):
        self.lines = lines  # Init inchangé

    def run(self):
        return sum(int(r) - int(l) for l, r in (line.split() for line in self.lines))

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    decrypt = Decrypt(lines)
    solution = decrypt.run()
    print(solution)
