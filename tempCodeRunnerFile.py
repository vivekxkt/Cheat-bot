import tkinter as tk
import os
import time
import pyautogui
from pynput import keyboard

DATA_DIR = "data"

current_lines = []
current_index = 0

def read_text_file(name):
    path = os.path.join(DATA_DIR, name)
    if not os.path.exists(path):
        print("File not found:", path)
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()

def type_next_line():
    global current_index, current_lines

    if current_index >= len(current_lines):
        print("Finished all lines.")
        return

    line = current_lines[current_index].lstrip()  # REMOVE EXTRA INDENT
    current_index += 1

    time.sleep(0.2)
    pyautogui.write(line, interval=0.02)
    pyautogui.press("enter")

    print("Typed:", line)


def small_window():
    root = tk.Tk()
    root.title("Helper")
    root.geometry("220x70")
    root.attributes("-topmost", True)

    entry = tk.Entry(root)
    entry.pack(pady=5)

    def submit():
        global current_lines, current_index

        filename = entry.get().strip()
        if not filename.endswith(".txt"):
            filename += ".txt"

        lines = read_text_file(filename)
        if not lines:
            root.destroy()
            return

        current_lines = lines
        current_index = 0

        print(f"Loaded {len(lines)} lines from {filename}.")
        print("Press F8 to type next line.")
        root.destroy()

    tk.Button(root, text="Load", command=submit).pack()
    root.mainloop()

def listen_hotkeys():
    def on_press(key):
        if key == keyboard.Key.f8:
            type_next_line()

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

small_window()
listen_hotkeys()



