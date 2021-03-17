from pynput.keyboard import Listener, Key, Controller

def on_press(key):
    print(f'you pressed: {str(key)}')
    if key == Key.esc:
        exit()
    
listener = Listener(on_press=on_press)
listener.start()
listener.join()
