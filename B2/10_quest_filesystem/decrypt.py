class Decrypt:
    def __init__(self, lines: list):
        self.lines = lines
        
    def run(self):
        # Clean up the lines
        self.lines = [line.rstrip() for line in self.lines if line.strip()]
        
        # Build a file system tree
        fs_tree = {}
        current_path = []
        
        for line in self.lines:
            # Calculate the depth based on indentation
            indent = (len(line) - len(line.lstrip())) // 2
            
            # Adjust current path based on indent level
            current_path = current_path[:indent]
            
            content = line.strip()
            
            if content.endswith('/'):  # This is a directory
                dir_name = content[2:-1]  # Remove "- " and trailing "/"
                current_path.append(dir_name)
                
                # Create nested dict for the directory
                current = fs_tree
                for dir_part in current_path[:-1]:
                    if dir_part not in current:
                        current[dir_part] = {}
                    current = current[dir_part]
                current[dir_name] = {}
            else:  # This is a file
                file_parts = content[2:].split(' (')
                file_name = file_parts[0]
                file_size = int(file_parts[1].split(' bytes')[0])
                
                # Add file to current directory
                current = fs_tree
                for dir_part in current_path:
                    if dir_part not in current:
                        current[dir_part] = {}
                    current = current[dir_part]
                current[file_name] = file_size
        
        # Calculate directory sizes
        dir_sizes = {}
        self._calculate_dir_sizes(fs_tree, '', dir_sizes)
        
        # Sum directories with size at most 100,000 bytes
        total_size = 0
        for _, size in dir_sizes.items():
            if size <= 100000:
                # print(f"Directory size: {size} bytes")
                total_size += size
                
        return total_size
    
    def _calculate_dir_sizes(self, node, path, dir_sizes):
        """Calculate the size of a directory and its subdirectories recursively"""
        dir_size = 0
        
        for name, content in node.items():
            if isinstance(content, dict):  # It's a directory
                subdir_path = f"{path}/{name}" if path else name
                subdir_size = self._calculate_dir_sizes(content, subdir_path, dir_sizes)
                dir_size += subdir_size
            else:  # It's a file
                dir_size += content
        
        if path:  # Don't store size for the root
            dir_sizes[path] = dir_size
            
        # print(f"Directory: {path}, Size: {dir_size} bytes")
        return dir_size
    
if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    decrypt = Decrypt(lines)
    solution = decrypt.run()
    print(solution)

