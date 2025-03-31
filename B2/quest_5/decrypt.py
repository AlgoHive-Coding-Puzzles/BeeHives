class Decrypt:
    def __init__(self, lines: list):
        self.lines = lines

    def run(self):
        seen = set()
        pairs = []
        for num in self.lines:
            complement = self.lines[0] - num
            if complement in seen:
                pairs.append((min(num, complement), max(num, complement)))  # Ensure no duplicates
            seen.add(num)
        return pairs

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    decrypt = Decrypt(lines)
    solution = decrypt.run()
    print(solution)
