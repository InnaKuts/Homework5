from pathlib import Path
from utility.pretty_path import print_directory_tree 
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py /path/to/directory")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"Error: The path {directory_path} does not exist.")
        sys.exit(1)
    
    if not directory_path.is_dir():
        print(f"Error: The path {directory_path} is not a directory.")
        sys.exit(1)

    print_directory_tree(directory_path)

if __name__ == "__main__":
    main()