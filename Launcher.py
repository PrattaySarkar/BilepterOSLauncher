import os
import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import ImageTk, Image
import pygame
from ttkthemes import ThemedTk


def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def interpolate_color(color1, color2, factor):
    return (
        int(color1[0] + (color2[0] - color1[0]) * factor),
        int(color1[1] + (color2[1] - color1[1]) * factor),
        int(color1[2] + (color2[2] - color1[2]) * factor)
    )

def update_colors():
    global step, current_color, next_color, color_index
    factor = step / steps

    interpolated_color = interpolate_color(current_color, next_color, factor)
    hex_color = rgb_to_hex(*interpolated_color)

    for frame in color_frames:
        frame.config(bg=hex_color)

    step += 1
    if step > steps:
        step = 0
        current_color = next_color
        color_index = (color_index + 1) % len(colors)
        next_color = colors[color_index]

    root.after(update_interval, update_colors)


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


colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255)   # Magenta
]

steps = 100
update_interval = 20
step = 0
color_index = 0

current_color = colors[color_index]
next_color = colors[(color_index + 1) % len(colors)]

# Create thin frames around the window
frame_thickness = 5

top_frame = tk.Frame(root, height=frame_thickness)
top_frame.pack(side="top", fill="x")

bottom_frame = tk.Frame(root, height=frame_thickness)
bottom_frame.pack(side="bottom", fill="x")

left_frame = tk.Frame(root, width=frame_thickness)
left_frame.pack(side="left", fill="y")

right_frame = tk.Frame(root, width=frame_thickness)
right_frame.pack(side="right", fill="y")

# Store frames for easy color update
color_frames = [top_frame, bottom_frame, left_frame, right_frame]

# Start updating colors
update_colors()

root.tk.call('source', 'forest-dark.tcl')
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
