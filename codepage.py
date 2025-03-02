import time
import tkinter as tk
import ttkbootstrap as ttk
import pyperclip
import subprocess

# The 16x16 symbol array
symbols = [
    ["¡", "¢", "£", "¤", "¥", "¦", "©", "¬", "®", "µ", "½", "¿", "€", "Æ", "Ç", "Ð"],
    ["Ñ", "×", "Ø", "Œ", "Þ", "ß", "æ", "ç", "ð", "ı", "ȷ", "ñ", "÷", "ø", "œ", "þ"],
    [" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/"],
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?"],
    ["@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"],
    ["P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_"],
    ["`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
    ["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "¶"],
    ["°", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹", "⁺", "⁻", "⁼", "⁽", "⁾", "Ɓ"],
    ["Ƈ", "Ɗ", "Ƒ", "Ɠ", "Ƙ", "Ɱ", "Ɲ", "Ƥ", "Ƭ", "Ʋ", "Ȥ", "ɓ", "ƈ", "ɗ", "ƒ", "ɠ"],
    ["ɦ", "ƙ", "ɱ", "ɲ", "ƥ", "ʠ", "ɼ", "ʂ", "ƭ", "ʋ", "ȥ", "Ạ", "Ḅ", "Ḍ", "Ẹ", "Ḥ"],
    ["Ị", "Ḳ", "Ḷ", "Ṃ", "Ṇ", "Ọ", "Ṛ", "Ṣ", "Ṭ", "Ụ", "Ṿ", "Ẉ", "Ỵ", "Ẓ", "Ȧ", "Ḃ"],
    ["Ċ", "Ḋ", "Ė", "Ḟ", "Ġ", "Ḣ", "İ", "Ŀ", "Ṁ", "Ṅ", "Ȯ", "Ṗ", "Ṙ", "Ṡ", "Ṫ", "Ẇ"],
    ["Ẋ", "Ẏ", "Ż", "ạ", "ḅ", "ḍ", "ẹ", "ḥ", "ị", "ḳ", "ḷ", "ṃ", "ṇ", "ọ", "ṛ", "ṣ"],
    ["ṭ", "§", "Ä", "ẉ", "ỵ", "ẓ", "ȧ", "ḃ", "ċ", "ḋ", "ė", "ḟ", "ġ", "ḣ", "ŀ", "ṁ"],
    ["ṅ", "ȯ", "ṗ", "ṙ", "ṡ", "ṫ", "ẇ", "ẋ", "ẏ", "ż", "«", "»", "‘", "’", "“", "”"]
]

# Create main application window
root = ttk.Window(title="Jelly Symbol Grid", themename="darkly")

def insert_symbol(symbol: str) -> None:
    pyperclip.copy(symbol)
    root.withdraw()
    time.sleep(0.2)
    subprocess.run(["xdotool", "key", "XF86Paste"])
    time.sleep(0.1)
    root.deiconify()
    
    

# Create 16x16 grid of buttons
for r in range(16):
    for c in range(16):
        btn = ttk.Button(root, text=symbols[r][c], width=2,
                        command=lambda s=symbols[r][c]: insert_symbol(s))
        btn.grid(row=r, column=c)

root.mainloop()
