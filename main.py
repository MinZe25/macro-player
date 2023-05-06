import keyboard
import mouse
import time
import sys


def click(x: int, y: int, double=False, left=True):
    mouse.move(x, y, True)
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
    keyboard.on_press_key("esc", stop_program)
    wait(500)
    times = int(sys.argv[1]) if len(sys.argv) >= 2 else 1
    print(f"executing {times} times")
    with open('./input.csv', 'r') as file:
        inp = [line.replace('"', '').split(';') for line in file.read().splitlines()]
    for i in range(times):
        print(f"{i} iteration:\n\n")
        for act, val, _ in inp:
            if stop:
                print('Stopping the program')
                exit(1)
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
    start()
