import os
import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import ImageTk, Image
import pygame

# Back Ground M.U.S.I.C.

pygame.mixer.init()

pygame.mixer.music.load("somebackgroundmusic.mp3")
pygame.mixer.music.play(-1)

def launchercredits():
    new_window = tk.Toplevel(root)
    new_window.title("Credits - BilepterOS Launcher")
    new_window.geometry("400x200")
    new_window.resizable(False, False)

    label1 = tk.Label(new_window, text="Credits", anchor='nw', justify='center', font=("Arial", 20),
                      width=80, height=1)
    label1.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    label2 = tk.Label(new_window, text="Main Programmer: PrattaySarkar (aka. FiredUpAviation)", anchor='n',
                      justify='center', font=("Arial", 10), width=80, height=1)
    label2.pack(padx=1, pady=1, fill=tk.BOTH, expand=True)

    label2 = tk.Label(new_window, text="Idea and Prototype: Prajeet Som Chauduri (aka. Wateredvition)", anchor='n',
                      justify='center', font=("Arial", 10), width=80, height=1)
    label2.pack(padx=1, pady=1, fill=tk.BOTH, expand=True)


def install_qemu():
    webbrowser.open("https://github.com/PrattaySarkar/BilepterOS/blob/main/README.md")


def launchv1():
    os.system("qemu-system-x86_64 imgs\\\\bilepteros1.bin")


def launchv2():
    os.system("qemu-system-x86_64 imgs\\\\bilepteros2.iso")


def perform_action():
    selected_option = listbox.get(listbox.curselection())
    if selected_option == "BilepterOS v1.0":
        launchv1()
    elif selected_option == "BilepterOS v2.0":
        launchv2()


root = tk.Tk()
root.title("BilepterOS Launcher")
root.geometry("300x550")

# Import the tcl file
root.tk.call('source', 'forest-dark.tcl')

# Set the theme with the theme_use method
ttk.Style().theme_use('forest-dark')

root.resizable(False, False)

image_path = 'transparentlogo1.png'
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo, bg='black')
image_label.pack(pady=10)

output_label = tk.Label(root, text="BilepterOS Launcher", anchor='nw', justify='center', font=("Arial", 20),
                        width=80, height=1)
output_label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

listbox = tk.Listbox(root, height=5)
options = ["BilepterOS v1.0", "BilepterOS v2.0"]
for option in options:
    listbox.insert(tk.END, option)
listbox.pack(pady=10)

button = ttk.Button(root, text="Launch OS", style="Accent.TButton", command=perform_action)
button.pack(pady=10)

output_label2 = tk.Label(root, text="NOTE: QEMU is Needed to Run This!", anchor='nw', justify='center',
                         font=("Arial", 10),
                         width=80, height=0)
output_label2.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

button2 = ttk.Button(root, text="QEMU Installation Tutorial", style="Accent.TButton", command=install_qemu)
button2.pack(pady=10)

button3 = ttk.Button(root, text="Credits", style="Accent.TButton", command=launchercredits)
button3.pack(pady=10)


def on_closing():
    pygame.mixer.music.stop()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
