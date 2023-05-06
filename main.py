import keyboard
import mouse
import time
import sys


def click(x: int, y: int, double=False, left=True):
    mouse.move(x, y)
    but = mouse.LEFT if left else mouse.RIGHT
    if double:
        mouse.double_click(but)
    else:
        mouse.click(but)


def key_press(key: str):
    keyboard.press_and_release(key)


def wait(ms: int):
    time.sleep(ms / 1000)


def start():
    with open('./input.csv', 'r') as file:
        inp = file.read().splitlines()
    for line in inp:
        act, val, _ = line.replace('"', '').split(';')
        if act == "Key press" or act == "Character(s)":
            print(line)
            key_press(val)
        elif act == "Wait":
            print(line)
            wait(int(val.split(' ')[0]))
        elif act == "Mouse left double click":
            print(line)
            x, y = [int(x) for x in val.replace(' ', '').split(',')]
            click(x, y, True)
        elif act == "Mouse left click":
            print(line)
            x, y = [int(x) for x in val.replace(' ', '').split(',')]
            click(x, y, False)


if __name__ == "__main__":
    start()
