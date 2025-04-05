class Decrypt:
    def __init__(self, lines: list):
        self.lines = lines

    def run(self):
        total_vowels = 0
        vowels = "aeiouy"
        for line in self.lines:
            total_vowels += sum(1 for char in line if char in vowels)
        return total_vowels

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    decrypt = Decrypt(lines)
    solution = decrypt.run()
    print(solution)
