from pathlib import Path
from colorama import init, Fore, Style

def print_directory_tree(path, indent = ""):
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}/")
                print_directory_tree(item, indent + "    ")
            else:
                print(f"{indent}{Fore.YELLOW}{item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Permission Denied{Style.RESET_ALL}")
