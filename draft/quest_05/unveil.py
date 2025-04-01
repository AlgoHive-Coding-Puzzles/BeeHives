class Unveil:
    def __init__(self, lines: list):
        self.lines = lines

    def run(self):
        total = 0
        for line in self.lines:
            num1, num2 = map(int, line.split())
            common_factors = self.get_common_factors(num1, num2)
            product = 1
            for factor in common_factors:
                product *= factor  # Multiply the common factors together
            total += product
        return total
    
    def get_common_factors(self, num1, num2):
        factors1 = {i for i in range(1, num1 + 1) if num1 % i == 0}
        factors2 = {i for i in range(1, num2 + 1) if num2 % i == 0}
        return factors1 & factors2  # Return common factors

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    unveil = Unveil(lines)
    solution = unveil.run()
    print(solution)
