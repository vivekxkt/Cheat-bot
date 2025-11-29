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

Clone the repository: [ Terminal ]
-> git clone https://github.com/yourusername/CheatBot.git
-> cd CheatBot

OR 

 [ Just download the exe from the provided RELEASE and run on windows without any compiler ]

 SCREEN SHOTS WITH USAGE :

1) Open the bot from start menu or RUN or whereever the exe is.
 <img width="184" height="151" alt="Screenshot 2025-11-29 145358" src="https://github.com/user-attachments/assets/ba72bad3-b276-4b6e-abef-e6d6557e9621" />

2) Now a black small popup will appear at the top left corner of the screen 
<img width="436" height="299" alt="Screenshot 2025-11-29 145459" src="https://github.com/user-attachments/assets/103431f2-d0a5-45aa-a10d-fc3840a24b71" />

3) Now type name of the file among the following files I've already created without the .TXT extension and hit ENTER ( you can create your own files )
<img width="203" height="527" alt="image" src="https://github.com/user-attachments/assets/2d808126-842c-4783-adfd-f797ab6ff9a4" />

4) For example I type : BUBBLE and hit ENTER key
<img width="454" height="284" alt="Screenshot 2025-11-29 145505" src="https://github.com/user-attachments/assets/82fdd43e-4bf5-4f74-8d61-b484262540bc" />

5) If The bot disappear from the top left corner that means the file exist and it will start running int the background (you can see in your system tray )
<img width="543" height="270" alt="Screenshot 2025-11-29 145537" src="https://github.com/user-attachments/assets/da3462fc-910d-40cd-a87e-5e17eafd7c38" />  

6) The bot will now read all the lines from bubble sort file
<img width="607" height="790" alt="image" src="https://github.com/user-attachments/assets/0ff55f7b-fa4a-419a-ae89-85c90be598a9" />

7) Now open a temporary empty file 
<img width="609" height="543" alt="Screenshot 2025-11-29 145646" src="https://github.com/user-attachments/assets/3c2217ae-083b-4183-828d-92245b0e5854" />

8) Now press the HOTKEY : F8 OR (fn + F8) AND SEE THE MAGIC
<img width="579" height="565" alt="Screenshot 2025-11-29 145637" src="https://github.com/user-attachments/assets/c6d0f2cb-acf2-4bfe-a669-23f02eb3c193" />

The bot will now write the code line by line everytime you hit the F8 key and to exit the bot You can EITHER press F10 or (Fn + F10 ) HOTKEY or just 
simply Quit the running bot from the system tray.



If you want to run the program from terminal : 

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
