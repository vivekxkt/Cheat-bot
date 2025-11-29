# 🛠️ CheatBot — A Fast Auto-Typing Helper Bot

CheatBot is a lightweight, tray-based helper bot that automatically types lines from a selected `.txt` file using a hotkey.  
It’s designed for speed, simplicity, and staying completely out of your way.

Perfect for coding, note-taking, exam-style typing practice, or any workflow where you need to paste structured lines one after another with a hotkey.

---

## 🚀 Features

- ⚡ **Auto-type any text file line-by-line**  
- 🖱️ **System tray icon** (silent background operation)  
- 🧠 **Hotkey support:**  
  - `F8` → Type the next line  
  - `F10` → Quit the bot  
- 📂 **Auto-loads .txt file from the `/data` folder**  
- 🖥️ **Custom minimal UI window** to enter filename  
- 🎨 **Dynamic tray icon generated using Pillow**  
- ✔️ **PyInstaller-friendly packaging** (works in `--onefile`)  
- 🧬 Fully threaded, stable, non-blocking  
- 🌑 Custom draggable title bar with no default border  

---

## 📦 Folder Structure

project/
│── bot.py
│── data/
│ └── *.txt # text files the bot types
│── app.ico # installer icon
│── Installer.iss # Inno Setup script (optional)
└── dist/
└── bot.exe (generated after PyInstaller build)

---

## 🖥️ How It Works

1. Run the bot → tray icon appears  
2. A small custom UI pops up asking for a filename  
3. Enter something like: BST

(The bot will load `BST.txt` automatically)  
4. Focus your cursor anywhere (VS Code, Notepad, browser, etc.)  
5. Press `F8` → the bot types the next line  
6. Repeat until all lines are done  
7. Use tray → Quit OR press `F10`  

---

## 🔑 Hotkeys

| Hotkey | Action |
|--------|--------|
| **F8** | Type next line |
| **F10** | Quit bot immediately |

---

## 🛠️ Installation (From Source)

Clone the repository:

```bash
git clone https://github.com/yourusername/CheatBot.git
cd CheatBot

Install required libraries: pip install pystray pillow pynput pyautogui
 
Run the bot: python bot.py


📦 Building an EXE (PyInstaller)

You can generate a standalone EXE using:

pyinstaller --onefile --noconsole ^
 --add-data "data;data" ^
 --hidden-import=pynput ^
 --hidden-import=pyautogui ^
 --hidden-import=pystray bot.py


📝 Requirements

Windows 10/11

Python 3.8+ (for development)

Permissions to access system tray + hotkeys

🤝 Contributing

PRs are welcome!
If you have ideas for new features (auto-start, better UI, presets, etc.), feel free to open an issue.

📄 License

This project is open-source and free to use.
No restrictions — modify, share, learn, enjoy.

⭐ Support

If this bot helped you, consider giving the repo a star ⭐ — it motivates further improvements!
