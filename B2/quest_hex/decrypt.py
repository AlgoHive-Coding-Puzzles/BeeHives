class Decrypt:
    def __init__(self, lines: list):
        self.lines = lines
        
    def determine_closest_color(self, hex_color: str) -> int:
        # Remove '#' if present
        if hex_color.startswith('#'):
            hex_color = hex_color[1:]
        
        # Parse the hex color to get the RGB components
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        
        # Calculate the distance to each pure color
        # Pure Red (255, 0, 0)
        dist_to_red = ((r - 255) ** 2 + g ** 2 + b ** 2) ** 0.5
        
        # Pure Green (0, 255, 0)
        dist_to_green = (r ** 2 + (g - 255) ** 2 + b ** 2) ** 0.5
        
        # Pure Blue (0, 0, 255)
        dist_to_blue = (r ** 2 + g ** 2 + (b - 255) ** 2) ** 0.5
                
        # Determine the closest color with priority for equidistant colors
        if dist_to_red <= dist_to_green and dist_to_red <= dist_to_blue:
            return 'red'
        elif dist_to_green <= dist_to_blue:
            return 'green'
        else:
            return 'blue'
    
    def run(self):
        vote_count = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for i in range(len(self.lines)):
            # Remove leading and trailing whitespace
            self.lines[i] = self.lines[i].strip()
            # Add the color to the vote count
            vote_count[self.determine_closest_color(self.lines[i])] += 1
            
        new_hexa = self.build_new_hexa(vote_count['red'], vote_count['green'], vote_count['blue'])
        print(new_hexa)
        return self.convert_hexa_to_int(new_hexa)
        
    def build_new_hexa(self, r, g, b):
        """Build a new hex color from RGB values, if the values are too high, we do a modulo 256"""
        r = r % 256
        g = g % 256
        b = b % 256
        print(f'RGB: #{r:02X}{g:02X}{b:02X}')
        return f'#{r:02X}{g:02X}{b:02X}'
    
    def convert_hexa_to_int(self, hexa):
        """Convert a hex color to an int"""
        hexa = hexa.lstrip('#')
        return int(hexa, 16)
            
if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    decrypt = Decrypt(lines)
    solution = decrypt.run()
    print(solution)

