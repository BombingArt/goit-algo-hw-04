import sys
from colorama import Fore, Style
from pathlib import Path


def print_structure(path: str, indent: int = 0):
    directory = Path(path)
    if directory.is_dir():
        print('|   ' * indent + '|- 📂', Fore.LIGHTRED_EX + directory.name, Style.RESET_ALL)
        for item in directory.iterdir():
            if item.is_dir():
                print_structure(item, indent + 1)
            else:
                print('|   ' * (indent + 1) + '|- 📜', Fore.LIGHTYELLOW_EX + item.name, Style.RESET_ALL)
    else:
        print('|   ' * indent + '|- 📜', Fore.LIGHTYELLOW_EX + directory.name, Style.RESET_ALL)




def main():
    dir_path = sys.argv[1]    
    print_structure(dir_path)

if __name__ == '__main__':
    main()
