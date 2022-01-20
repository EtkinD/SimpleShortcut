from pynput.keyboard import Listener, Controller
from .ShortcutKeys import press_keys
from time import sleep

if __name__ == '__main__':
    input('This script can not be executed.\nPress any key to exit.')
    exit(0)


class _SimpleShortcut:
    """
    Handles all the shortcut processes.
    - Listens user keyboard.
    - Reads 'shortcuts.txt'
    - Parses combos
    - and presses keys
    """
    _fn_code = '<255>'
    _fn_pressed = False
    _last_key = 'There is no key.'
    _press = Controller()

    def __init__(self, shortcut_file_path: str, auto_start: bool):
        self.shortcut_file_path = shortcut_file_path
        self._listener = Listener(on_press=self._on_press, on_release=self._on_release)
        if auto_start:
            self.start()
            self.join()

    def _on_press(self, key):
        """
        Runs when user presses a key.
        """
        if str(key) == self._fn_code:
            self._fn_pressed = True
        elif self._fn_pressed and self._last_key == 'There is no key.':
            self._last_key = str(key)
            self._execute()

    def _on_release(self, key):
        """
        Runs when user releases a key.
        """
        if str(key) == self._fn_code:
            self._fn_pressed = False
        elif str(key) == self._last_key:
            self._last_key = 'There is no key.'

    def _read_shortcuts(self) -> list:
        """
        reads 'shortcuts.txt' file and returns all the lines in a list (Except comments and empty lines)
        :return: list of lines in 'shortcuts.txt' file
        """
        result = list()
        try:
            lines = list()
            with open(self.shortcut_file_path, 'r') as file:
                lines = file.readlines()

            assert len(lines) != 0

            for i in range(len(lines)):
                lines[i] = lines[i].strip()
                if len(lines[i]) > 0 and lines[i][0] != '#':
                    result.append(lines[i].strip())
            return result
        except:
            input('A problem occurred while reading "shortcuts.txt" file.\nPlease check file exists or not.\nOr it may be unreadable file.')
            return result

    def _execute(self):
        """
        Checks shortcuts if there is one for the pressed key after fn button.
        If there is, passes combos to '_handle_combos' method.
        """
        # clearing "'" from key string.
        pressed_key = self._last_key[1:-1]

        for line in self._read_shortcuts():
            line = line.split(sep='=')
            # index 0: key
            # index 1: shortcut keys

            if line[0] == pressed_key:
                self._handle_combos(line[1].split(sep=' -> '))
                break

    def _handle_combos(self, combos: list):
        """
        Parses combos and sends keys to '_press_keys' method between 0.01 seconds of sleeps.
        :param combos: Combo keys that separated with ' -> '
        """
        for combo in combos:
            self._press_keys(combo.split(sep='+'))
            sleep(0.01)

    def _press_keys(self, keys: list):
        """
        Starts pressing all the keys from first key to last key, and releases them from last key to first key.
        :param keys: Keys of a single combo.
        """
        if len(keys) == 0 or keys[0] == '':
            return

        if press_keys.get(keys[0]) is not None:
            print(press_keys.get(keys[0]))
            with self._press.pressed(press_keys.get(keys[0])):
                keys.pop(0)
                self._press_keys(keys)
        else:
            with self._press.pressed(keys[0]):
                keys.pop(0)
                self._press_keys(keys)

    def start(self):
        """
        Starts listener.
        :return: This handler class
        """
        self._listener.start()
        return self

    def join(self):
        """
        Joins listener.
        :return: This class
        """
        self._listener.join()
        return self


def run(shortcut_file_path: str, auto_start: bool = True) -> _SimpleShortcut:
    """
    Initializes Shortcut handler class and returns it.
    :param auto_start: If true, shortcut handler will start listening keys and join listener automatically.
    Else, it won't start listening or join listener.
    :param shortcut_file_path: file path that contains user's shortcuts.
    :return: Shortcut handler class
    """
    return _SimpleShortcut(shortcut_file_path=shortcut_file_path, auto_start=auto_start)
