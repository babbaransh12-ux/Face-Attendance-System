import tkinter as tk
from tkinter import messagebox

def get_buttnon(window, text, color, command, fg='white'):
    button = tk.button(
        window,
        text=text,
        fg=fg,
        bg=color,
        command=command,
        height=2,
        wodth=20,
        font=("Helvetica bold", 20)
    )
    return button

def get_img_label(window):
    label = tk.label(window)
    label.grid(row=0, column=0)
    return label

def get_text_label(window, text):
    label = tk.Label(window, text=text)
    label.config(font=("sans-serif",21), justify="left")
    return label

