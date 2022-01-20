# Simple Shortcut

## Description

This repository has been created to add custom shortcuts by pressing 'fn' button.

## Requirements

- Python3 sdk
- Pip3 (python package manager)
- 'pynput' library

## Installing requirements with pip

If you use your default interpreter directly run the code below.
If you use virtual environment run the code after activating virtual environment. 

```shell
pip3 install pynput
```

## Run

After installing 'pynput' library, you can run the main.py script by using below code.

```shell
python3 main.py
```

## Adding shortcuts and usage

You can find usage of the program from the 'shortcuts.txt' file.

## Testing keys

There is 'test.py' file under root directory. You can run this file to test your keyboard's
keycodes.

```shell
python3 test.py
```

When pressing fn key it must print '<255>' on the terminal. If it is different,
please open ```lib/SimpleShortcut.py``` in a text editor and change line 18 with your output.

While test.py is running, pressing escape button terminates it.

## Announcement

This repository is not maintaining anymore.
If you like to contribute or maintain this repository,
you can contact with me or directly create merge requests.
