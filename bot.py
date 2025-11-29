# bot.py
# Requires: pystray, pillow, pynput, pyautogui
# pip install pystray pillow pynput pyautogui

import tkinter as tk
import os
import time
import pyautogui
from pynput import keyboard
import threading
from PIL import Image, ImageDraw, ImageFont
import pystray  # type: ignore
import sys

DATA_DIR_NAME = "data"  # folder name inside project and also bundled

txt_lines = []
txt_index = 0
hotkey_listener = None
tray_icon = None

# ----------------------------------------------------------
# Helper: path that works both in normal run and PyInstaller
# ----------------------------------------------------------
def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller onefile/onedir.
    Example: resource_path(os.path.join('data', 'BST.txt'))
    """
    if getattr(sys, "frozen", False):
        # running in a bundle (PyInstaller)
        base_path = sys._MEIPASS  # where PyInstaller extracts files
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


# ----------------------------------------------------------
# Load TXT file
# ----------------------------------------------------------
def load_txt(name):
    global txt_lines, txt_index

    # Name expected like "BST.txt"
    rel = os.path.join(DATA_DIR_NAME, name)
    path = resource_path(rel)

    if not os.path.exists(path):
        print("❌ File not found:", path)
        return False

    with open(path, "r", encoding="utf-8") as f:
        raw = f.read().splitlines()

    cleaned = []
    for line in raw:
        line = line.rstrip()
        if line.strip() == "":
            continue
        cleaned.append(line.strip())

    txt_lines = cleaned
    txt_index = 0

    print(f"✔ Loaded {len(txt_lines)} lines from {name}")
    return True


# ----------------------------------------------------------
# Type NEXT line from TXT file + show preview
# ----------------------------------------------------------
def type_next_line():
    global txt_index, txt_lines

    if not txt_lines:
        print("❌ No file loaded. Load a .txt file first.")
        return

    if txt_index >= len(txt_lines):
        print("✔ Finished all lines.")
        return

    line = txt_lines[txt_index]

    if txt_index + 1 < len(txt_lines):
        print("Next:", txt_lines[txt_index + 1])
    else:
        print("Next: <END>")

    print("Typing:", line)

    txt_index += 1

    time.sleep(0.15)
    pyautogui.write(line, interval=0.02)
    pyautogui.press("enter")


# ----------------------------------------------------------
# GUI: choose TXT file
# ----------------------------------------------------------
def small_window():
    root = tk.Tk()
    root.title("Helper Bot")
    root.geometry("250x140")
    root.configure(bg="black")
    root.attributes("-topmost", True)

    # REMOVE default title bar
    root.overrideredirect(True)

    # ------------ CUSTOM TITLE BAR ------------
    title_bar = tk.Frame(root, bg="black", relief="flat", height=22)
    title_bar.pack(fill="x", side="top")

    title_label = tk.Label(
        title_bar,
        text="Helper Bot",
        bg="black",
        fg="white",
        font=("Arial", 10)
    )
    title_label.pack(side="left", padx=8)

    # --- CLOSE BUTTON ---
    close_btn = tk.Button(
        title_bar,
        text="✕",
        font=("Arial", 10, "bold"),
        bg="black",
        fg="white",
        bd=0,
        command=root.destroy,
        activebackground="red",
        activeforeground="white"
    )
    close_btn.pack(side="right", padx=5)

    # --- MINIMIZE BUTTON ---
    def minimize():
        root.update_idletasks()
        root.overrideredirect(False)
        root.iconify()

    min_btn = tk.Button(
        title_bar,
        text="—",
        font=("Arial", 10, "bold"),
        bg="black",
        fg="white",
        bd=0,
        command=minimize,
        activebackground="gray20",
        activeforeground="white"
    )
    min_btn.pack(side="right")

    # --- DRAG WINDOW FUNCTIONALITY ---
    def start_move(event):
        root.x = event.x
        root.y = event.y

    def stop_move(event):
        root.x = None
        root.y = None

    def on_motion(event):
        deltax = event.x - root.x
        deltay = event.y - root.y
        root.geometry(f"+{root.winfo_x() + deltax}+{root.winfo_y() + deltay}")

    title_bar.bind("<ButtonPress-1>", start_move)
    title_bar.bind("<ButtonRelease-1>", stop_move)
    title_bar.bind("<B1-Motion>", on_motion)

    # ------------ MAIN CONTENT ------------
    tk.Label(root, text="", bg="black", fg="white").pack(pady=(8, 5))

    entry = tk.Entry(
        root,
        font=("Arial", 12),
        bg="black",
        fg="white",
        insertbackground="white"
    )
    entry.pack(pady=2, padx=10, fill="x")
    entry.focus_set()

    status_label = tk.Label(root, text="", fg="white", bg="black", font=("Arial", 10))
    status_label.pack(pady=(4, 0))

    def submit(event=None):
        raw = entry.get().strip()
        filename = raw.replace(".c", "").replace(".txt", "").strip() + ".txt"
        if load_txt(filename):
            print("➡ Press F8 to type next line.")
            root.destroy()
        else:
            status_label.config(text="Invalid file!", fg="red")

    entry.bind("<Return>", submit)

    tk.Button(
        root,
        text="LOAD FILE",
        command=submit,
        font=("Arial", 8, "bold"),
        bg="white",
        fg="black",
        height=1
    ).pack(pady=6)

    root.mainloop()



# ----------------------------------------------------------
# Hotkey listener (F8)
# ----------------------------------------------------------
def listen_hotkeys():
    global hotkey_listener

    def on_press(key):
        try:
            # F8 → Type next line
            if key == keyboard.Key.f8:
                type_next_line()

            # F11 → Kill bot completely
            if key == keyboard.Key.f10:
                print("F11 pressed → exiting bot")
                on_quit(tray_icon)

        except Exception as e:
            print("Hotkey error:", e)

    hotkey_listener = keyboard.Listener(on_press=on_press)
    hotkey_listener.start()

# ----------------------------------------------------------
# Tray icon
# ----------------------------------------------------------
def create_image():
    """
    Create a 64x64 RGBA image for the tray icon.
    Uses a robust method to measure text across Pillow versions.
    """
    size = (64, 64)
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    bbox = (4, 4, size[0] - 4, size[1] - 4)
    draw.ellipse(bbox, fill=(30, 30, 30, 255))

    try:
        font = ImageFont.truetype("arial.ttf", 28)
    except Exception:
        font = ImageFont.load_default()

    text = "HB"

    # Try multiple ways to get text size to be compatible with Pillow versions
    try:
        # Newer Pillow: textbbox
        bbox_text = draw.textbbox((0, 0), text, font=font)
        w = bbox_text[2] - bbox_text[0]
        h = bbox_text[3] - bbox_text[1]
    except Exception:
        try:
            # Older Pillow: textsize
            w, h = draw.textsize(text, font=font)
        except Exception:
            try:
                # Font fallback
                w, h = font.getsize(text)
            except Exception:
                # Last resort: estimate
                w, h = (24, 24)

    # center and draw
    x = (size[0] - w) / 2
    y = (size[1] - h) / 2 - 2
    draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)
    return img


def on_quit(icon, item=None):
    try:
        if icon is not None:
            icon.stop()
    except Exception:
        pass
    try:
        global hotkey_listener
        if hotkey_listener is not None:
            hotkey_listener.stop()
    except Exception:
        pass
    print("Exiting…")
    os._exit(0)


def run_tray_icon():
    global tray_icon
    menu = pystray.Menu(pystray.MenuItem("Quit", lambda icon, item: on_quit(icon)))
    tray_icon = pystray.Icon("HelperBot", create_image(), "GPU inactive", menu)
    tray_icon.run()


# create/tray startup (use run_detached)
def run_tray_icon_detached():
    global tray_icon
    menu = pystray.Menu(pystray.MenuItem("Quit", lambda icon, item: on_quit(icon)))
    tray_icon = pystray.Icon("HelperBot", create_image(), "GPU inactive", menu)

    # Use run_detached() so pystray spawns its own thread/backend
    try:
        tray_icon.run_detached()
        print("Tray icon started (detached).")
    except Exception as e:
        print("Failed to start tray icon detached:", e)


# ----------------------------------------------------------
# RUN
# ----------------------------------------------------------
if __name__ == "__main__":
    # start tray icon detached (pystray handles its own thread)
    run_tray_icon_detached()

    # tiny pause to let OS register the tray icon (helps race conditions)
    time.sleep(0.6)

    # start hotkey listener
    listen_hotkeys()

    # show GUI to pick file
    try:
        small_window()
    except KeyboardInterrupt:
        print("Interrupted, quitting...")
        on_quit(tray_icon)

    print("Helper Bot running in tray. Press F8 to type next line, or use tray->Quit to exit.")

    # keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        on_quit(tray_icon)
