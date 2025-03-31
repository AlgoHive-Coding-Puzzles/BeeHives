class Unveil:
    def __init__(self, lines: list):
        self.lines = lines

    def run(self):
        seen = set()
        pairs = []
        for num in self.lines:
            complement = self.target - num
            if complement in seen:
                pairs.append((min(num, complement), max(num, complement)))  # Ensure no duplicates
            seen.add(num)
        return pairs

if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = list(map(int, f.readline().split()))
        target = int(f.readline())
    unveil = Unveil(numbers, target)
    solution = unveil.run()
    print(solution)
