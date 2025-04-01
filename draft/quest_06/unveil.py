class Unveil:
    def __init__(self, lines: list):
        self.lines = lines

    def run(self):
        # Extract target value from the first line
        target = int(self.lines[0].split(": ")[1])
        
        # Separate the pairs from the input
        left_col = []
        right_col = []
        
        unique_pairs = set()
        
        for line in self.lines[1:]:
            x, y = line.strip()[1:-1].split(", ")
            left_col.append(int(x))
            right_col.append(int(y))

        # Now find all pairs that sum to target
        for i in range(len(left_col)):
            if left_col[i] + right_col[i] == target:
                unique_pairs.add((min(left_col[i], right_col[i]), max(left_col[i], right_col[i])))
                
        for i in range(len(left_col)):
            for j in range(i + 1, len(left_col)):
                if left_col[i] + left_col[j] == target:
                    unique_pairs.add(min((left_col[i], left_col[j]), (left_col[j], left_col[i])))
        
        # Now we try to find all the unique pairs in the right_col only
        for i in range(len(right_col)):
            for j in range(i + 1, len(right_col)):
                if right_col[i] + right_col[j] == target:
                    unique_pairs.add(min((right_col[i], right_col[j]), (right_col[j], right_col[i])))
        
        return len(unique_pairs)

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    unveil = Unveil(lines)
    solution = unveil.run()
    print(solution)