from lib.SimpleShortcut import run
from os import path
from pathlib import Path


if __name__ == '__main__':
    shortcut_file_path = str(Path(__file__).parent) + path.sep + 'shortcuts.txt'
    print(f'The path of shortcuts\': {shortcut_file_path}')
    if not path.exists(shortcut_file_path):
        print('shortcut.txt file is not exists. Please create the file and run the script again.')
        exit(1)
    run(shortcut_file_path=shortcut_file_path, auto_start=True)
