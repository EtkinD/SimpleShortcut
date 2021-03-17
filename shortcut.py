from pynput.keyboard import Key, Listener, Controller
from os import path, system
from pathlib import Path
from time import sleep

def ifNotExists(path: str):
    with open(path, 'w', encoding='UTF-8') as f:
        f.write("""# Button code: alt_l -> left alt button
# Button code: alt_r -> right alt button (altgr)
#
# Button code: ctrl_l -> left ctrl button
# Button code: ctrl_r -> right ctrl button
#
# Button code: shift_l -> left shift button
# Button code: shift_r -> right shift button
#
# Button code: left -> left arrow button
# Button code: right -> right arrow button
# Button code: up -> up arrow button
# Button code: down -> down arrow button
#
# Button code: windows -> windows (super) button
#
# Button code: tab -> tab
# Button code: caps_lock -> caps lock
# Button code: esc -> escape
# Button code: delete -> delete
# Button code: backspace -> backspace
# Button code: space -> space
# Button code: enter -> enter
#
# Button code: f1, f2, f3, ...f20 -> f buttons from 1 to 20
#
# Laters and digits must be written exactly, it is sensitive uppercase and lowercase.
#
# More than one button combinations can be attached with ' -> ' (right and left spaces important!).
#
# Example: a=shift_l+tab -> alt_l+windows+right
# Full 
#
# Wrong example: a=shift_l+tab->alt_l+windows+right
#
# Including this line, all lines above are comment lines. program doesn't see these, because lines starts with '#'
# Default shortcuts:

d=ctrl_l+windows+d
a=ctrl_l+windows+left
s=ctrl_l+windows+right

# Example of ' -> '
f=alt_l+tab -> ctrl_l+windows+d -> alt_l+windows+left

z=windows+r kjasd jkhasdk aljksdlf ------ This line is a bad example.
x=alt_l+tab""")

class TwitchShortcutListener:

    def __init__(self, self_path: str = 'shortcuts.txt'):
        self.shortcuts_file_path = self_path
        self.listener = Listener(on_press=self.onPress, on_release=self.onRelease)
        self.press = Controller()
        self.fn = False
        self.done = True
        self.lastKey = 'there is no key while initialization.'
        self.join()

    def onPress(self, key):
        if str(key) == "'<255>'":
            self.fn = True
        # If fn is pressed it's okay but still the last pressed button isn't released,
        # it doesn't press same button thanks to self.done.
        if self.fn and self.done and str(key) != "'<255>'":
            self.done = False
            self.lastKey = str(key)
            self.parse(key)

    def onRelease(self, key):
        if str(key) == "'<255>'":
            self.fn = False
        if str(key) == self.lastKey:
            self.done = True
            self.lastKey = 'there is no key.'

    def parse(self, pressed_key):
        # Clearing pressed key's apostrophes.
        pressed_key = str(pressed_key)[1:-1]

        if not path.exists(self.shortcuts_file_path):
            ifNotExists(self.shortcuts_file_path)

        with open(self.shortcuts_file_path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            if len(line.strip()) == 0:
                continue
            if line.strip()[0] == '#':
                continue

            s = line.strip().split(sep='=')
            # index 0 is key
            # index 1 is shortcut keys

            if s[0] == pressed_key:
                keysThan = s[1].split(sep=' -> ')
                for m in keysThan:
                    print(f'Used shortcut: {m}  --  List that is included: {keysThan}')
                    keys = m.split(sep='+')
                    if keys[len(keys)-1].__contains__(' '):
                        k = ''
                        for i in keys[len(keys)-1]:
                            if i != ' ':
                                k += i
                            if i == ' ':
                                keys[len(keys) - 1] = k
                                break
                    self.cut(keys=keys)
                    # sleeps as less as possible
                    sleep(0.01)
                # Breaks file search cos key has found
                break

    def cut(self, keys: list):
        if len(keys) == 0:
            return
        if keys[0] == '':
            return

        if keys[0] == 'ctrl_l':
            keys.pop(0)
            with self.press.pressed(Key.ctrl_l):
                self.cut(keys)
            return
        elif keys[0] == 'ctrl_r':
            keys.pop(0)
            with self.press.pressed(Key.ctrl_r):
                self.cut(keys)
            return
        elif keys[0] == 'alt_l':
            keys.pop(0)
            with self.press.pressed(Key.alt_l):
                self.cut(keys)
            return
        elif keys[0] == 'alt_r':
            keys.pop(0)
            with self.press.pressed(Key.alt_r):
                self.cut(keys)
            return
        elif keys[0] == 'shift_l':
            keys.pop(0)
            with self.press.pressed(Key.shift_l):
                self.cut(keys)
            return
        elif keys[0] == 'shift_r':
            keys.pop(0)
            with self.press.pressed(Key.shift_r):
                self.cut(keys)
            return
        elif keys[0] == 'windows':
            keys.pop(0)
            with self.press.pressed(Key.cmd):
                self.cut(keys)
            return
        elif keys[0] == 'left':
            keys.pop(0)
            with self.press.pressed(Key.left):
                self.cut(keys)
            return
        elif keys[0] == 'right':
            keys.pop(0)
            with self.press.pressed(Key.right):
                self.cut(keys)
            return
        elif keys[0] == 'up':
            keys.pop(0)
            with self.press.pressed(Key.up):
                self.cut(keys)
            return
        elif keys[0] == 'down':
            keys.pop(0)
            with self.press.pressed(Key.down):
                self.cut(keys)
            return
        elif keys[0] == 'tab':
            keys.pop(0)
            with self.press.pressed(Key.tab):
                self.cut(keys)
            return
        elif keys[0] == 'caps_lock':
            keys.pop(0)
            with self.press.pressed(Key.caps_lock):
                self.cut(keys)
            return
        elif keys[0] == 'esc':
            keys.pop(0)
            with self.press.pressed(Key.esc):
                self.cut(keys)
            return
        elif keys[0] == 'delete':
            keys.pop(0)
            with self.press.pressed(Key.delete):
                self.cut(keys)
            return
        elif keys[0] == 'backspace':
            keys.pop(0)
            with self.press.pressed(Key.backspace):
                self.cut(keys)
            return
        elif keys[0] == 'space':
            keys.pop(0)
            with self.press.pressed(Key.space):
                self.cut(keys)
            return
        elif keys[0] == 'enter':
            keys.pop(0)
            with self.press.pressed(Key.enter):
                self.cut(keys)
            return
        elif keys[0] == 'f1':
            keys.pop(0)
            with self.press.pressed(Key.f1):
                self.cut(keys)
            return
        elif keys[0] == 'f2':
            keys.pop(0)
            with self.press.pressed(Key.f2):
                self.cut(keys)
            return
        elif keys[0] == 'f3':
            keys.pop(0)
            with self.press.pressed(Key.f3):
                self.cut(keys)
            return
        elif keys[0] == 'f4':
            keys.pop(0)
            with self.press.pressed(Key.f4):
                self.cut(keys)
            return
        elif keys[0] == 'f5':
            keys.pop(0)
            with self.press.pressed(Key.f5):
                self.cut(keys)
            return
        elif keys[0] == 'f6':
            keys.pop(0)
            with self.press.pressed(Key.f6):
                self.cut(keys)
            return
        elif keys[0] == 'f7':
            keys.pop(0)
            with self.press.pressed(Key.f7):
                self.cut(keys)
            return
        elif keys[0] == 'f8':
            keys.pop(0)
            with self.press.pressed(Key.f8):
                self.cut(keys)
            return
        elif keys[0] == 'f9':
            keys.pop(0)
            with self.press.pressed(Key.f9):
                self.cut(keys)
            return
        elif keys[0] == 'f10':
            keys.pop(0)
            with self.press.pressed(Key.f10):
                self.cut(keys)
            return
        elif keys[0] == 'f11':
            keys.pop(0)
            with self.press.pressed(Key.f11):
                self.cut(keys)
            return
        elif keys[0] == 'f12':
            keys.pop(0)
            with self.press.pressed(Key.f12):
                self.cut(keys)
            return
        elif keys[0] == 'f13':
            keys.pop(0)
            with self.press.pressed(Key.f13):
                self.cut(keys)
            return
        elif keys[0] == 'f14':
            keys.pop(0)
            with self.press.pressed(Key.f14):
                self.cut(keys)
            return
        elif keys[0] == 'f15':
            keys.pop(0)
            with self.press.pressed(Key.f15):
                self.cut(keys)
            return
        elif keys[0] == 'f16':
            keys.pop(0)
            with self.press.pressed(Key.f16):
                self.cut(keys)
            return
        elif keys[0] == 'f17':
            keys.pop(0)
            with self.press.pressed(Key.f17):
                self.cut(keys)
            return
        elif keys[0] == 'f18':
            keys.pop(0)
            with self.press.pressed(Key.f18):
                self.cut(keys)
            return
        elif keys[0] == 'f19':
            keys.pop(0)
            with self.press.pressed(Key.f19):
                self.cut(keys)
            return
        elif keys[0] == 'f20':
            keys.pop(0)
            with self.press.pressed(Key.f20):
                self.cut(keys)
            return
        else:
            k = keys.pop(0)
            # If program comes this lines, it means k must be one single character or number.
            # But if it has more characters than one, program will print an error line and will successfully continue processing.
            if len(k) != 1:
                print(f'You entered wrong button\nButton: {k}\nException reason: It is not one of special buttons such as cltr_l or f10 and contains more than one later.\nIf you want to enter more than one later, bind them with \'+\'.')
                print('Example:', end=' ')
                for t in k[:len(k)-1]:
                    print(f'{t}', end='+')
                print('' + k[len(k)-1])
                return
            with self.press.pressed(k):
                self.cut(keys)
            return

    def join(self):
        self.listener.start()
        self.listener.join()

if __name__ == '__main__':
    system('color 5')
    self_path = str(Path(__file__).parent) + path.sep + 'shortcuts.txt'
    print(f'The path of shortcuts\': {self_path}')
    if not path.exists(self_path):
        ifNotExists(self_path)
    listener = TwitchShortcutListener(self_path=self_path)
