import keyboard
import mouse
import time
import sys
from screeninfo import get_monitors
from ctypes import windll
from os import system
import ctypes

user32 = windll.user32
user32.SetProcessDPIAware()


def click(x: int, y: int, double=False, left=True):
    global monitor
    mouse.move(monitor.x + x, monitor.y + y, True)
    but = mouse.LEFT if left else mouse.RIGHT
    if double:
        mouse.double_click(but)
    else:
        mouse.click(but)


def key_press(key: str):
    keyboard.press_and_release(key)


def wait(ms: int):
    time.sleep(ms / 1000)


def print_act(act, val):
    print(f"{act} => {val}")


stop = False


def stop_program(a):
    global stop
    stop = True


def start():
    global stop
    global monitor
    keyboard.on_press_key("esc", stop_program)
    wait(500)
    times = int(sys.argv[1]) if len(sys.argv) >= 2 else 1
    print(f"executing {times} times")
    with open('input.csv', 'r') as file:
        inp = [line.replace('"', '').split(';') for line in file.read().splitlines()]
    for i in range(times):
        print(f"iteration {i}:\n\n")
        ctypes.windll.kernel32.SetConsoleTitleW(f"iteration {i}")
        for act, val, _ in inp:
            if stop:
                print('Stopping the program')
                exit(1)
            elif act == "Set Monitor":
                print_act(act, val)
                i = int(val)
                if len(monitors) > i:
                    monitor = monitors[i]
            elif act == "Key press" or act == "Character(s)":
                print_act(act, val)
                key_press(val)
            elif act == "Wait":
                print_act(act, val)
                wait(int(val.split(' ')[0]))
            elif act == "Mouse left double click":
                print_act(act, val)
                x, y = [int(x) for x in val.replace(' ', '').split(',')]
                click(x, y, True)
            elif act == "Mouse left click":
                print_act(act, val)
                x, y = [int(x) for x in val.replace(' ', '').split(',')]
                click(x, y, False)


if __name__ == "__main__":
    monitors = get_monitors()
    # uncomment the next lines to know what monitors do you have
    for m in monitors:
        print(m)
    monitor = next(m for m in monitors if m.is_primary)
    start()
