class Unveil:
    def __init__(self, lines: list):
        self.lines = lines  # Init inchangé

    def run(self):
        left_column = set()
        right_column = set()

        for line in self.lines:
            left, right = map(int, line.split())
            left_column.add(left)
            right_column.add(right)

        return sum(num for num in left_column if num in right_column)

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    unveil = Unveil(lines)
    solution = unveil.run()
    print(solution)
