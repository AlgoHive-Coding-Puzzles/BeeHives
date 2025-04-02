class Unveil:
    def __init__(self, lines: list):
        self.lines = lines

    def run(self):
        max_length = 0
        vowels = "aeiouy"
        for line in self.lines:
            current_length = 0
            longest_vowel_seq = 0
            for char in line:
                if char in vowels:
                    current_length += 1
                    longest_vowel_seq = max(longest_vowel_seq, current_length)
                else:
                    current_length = 0
            max_length = max(max_length, longest_vowel_seq)
        return max_length

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    unveil = Unveil(lines)
    solution = unveil.run()
    print(solution)
