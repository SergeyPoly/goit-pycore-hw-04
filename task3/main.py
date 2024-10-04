import sys
from pathlib import Path
from colorama import Fore, Style

def show_dir_structure(directory: Path, indent: int = 0) -> None:
    if directory.is_dir():
        print(Fore.BLUE + f"{'':<{indent}}{directory.name}/" + Style.RESET_ALL)
        indent +=4
        for path in sorted(directory.iterdir(), key=lambda p: (p.is_file(), p.name)):
            show_dir_structure(path, indent)

    else:
        print(Fore.GREEN + f"{'':<{indent}}{directory.name}" + Style.RESET_ALL)
            

if __name__ == "__main__":
    try:
        directory = Path(sys.argv[1])
        if not directory.exists() or not directory.is_dir():
            raise ValueError("Provided path is not a valid directory")
        
        show_dir_structure(directory)

    except IndexError:
        print(f"Warning: Missing path argument")
    except ValueError as e:
        print(f"Warning: {e}")
    except Exception as e:
        print(f"Something else went wrong: {e}")