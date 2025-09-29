import tkinter as tk
from tkinter import filedialog

# Window Setup 
window = tk.Tk()
window.title('File Encryption/Decryption')
window.geometry('600x400')
window.configure(background='#2E2E2E')  # dark grey background

# Styling 
BTN_BG = "#4CAF50"   # green
BTN_HOVER = "#45a049"
BTN_FG = "white"
BTN_FONT = ("Arial", 12, "bold")

# Top Label 
label = tk.Label(
    window,
    text="Encrypt or Decrypt Files",
    font=("Arial", 18, "bold"),
    bg="#2E2E2E",
    fg="white"
)
#So button can be seen
label.pack(pady=30)

# File Dialog Function
def open_file_dialog():
    filenames = filedialog.askopenfilenames()
    if filenames:
        print("Selected files:")
        for filename in filenames:
            print(filename)
    else:
        print("No files selected.")



# Decrypt Function 
def decrypt_files():
    print("Decrypt button pressed")


# Button Hover Effect
def on_enter(e):
    e.widget['background'] = BTN_HOVER

def on_leave(e):
    e.widget['background'] = BTN_BG



# Button Frame
button_frame = tk.Frame(window, bg="#2E2E2E")
button_frame.pack(pady=20)



# Encrypt Button
open_button = tk.Button(
    button_frame,
    text="Encrypt / Open Files",
    command=open_file_dialog,
    bg=BTN_BG,
    fg=BTN_FG,
    font=BTN_FONT,
    activebackground=BTN_HOVER,
    activeforeground=BTN_FG,
    relief="flat",
    width=18,
    height=2
)



# Side by side buttons
open_button.grid(row=0, column=0, padx=15)  

open_button.bind("<Enter>", on_enter)
open_button.bind("<Leave>", on_leave)


# Decrypt Button 
decrypt_button = tk.Button(
    button_frame,
    text="Decrypt Files",
    command=decrypt_files,
    bg=BTN_BG,
    fg=BTN_FG,
    font=BTN_FONT,
    activebackground=BTN_HOVER,
    activeforeground=BTN_FG,
    relief="flat",
    width=18,
    height=2
)


# Grid placement for buttons
decrypt_button.grid(row=0, column=1, padx=15)

decrypt_button.bind("<Enter>", on_enter)
decrypt_button.bind("<Leave>", on_leave)














# Keep Window Open
window.mainloop()
