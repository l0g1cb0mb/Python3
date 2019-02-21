import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title("Pyramid maker")
window_width = 180
window_height = 70
window.geometry(str(window_width)+"x"+str(window_height))


ttk.Label(window, text = "How many blocks do you have?").grid(column = 0, row = 0)

def close(event):
    window.withdraw()
    exit(0)

def click_me(event):
    height = 0
    tmp = int(blocks.get())

    while blocks:
        if ((height + 1) <= tmp):
            tmp -= (height + 1)
            height += 1
        else:
            break;

    messagebox.showinfo("Pyramid maker", "You have " + blocks.get() + " blocks and you can make a pyramid with a height of " + str(height))
    blocks.set("")
    blocks_entered.focus()

window.bind("<Return>", click_me)
window.bind("<Escape>", close)

blocks = tk.StringVar()
blocks_entered = ttk.Entry(window, width = 12, textvariable = blocks)
blocks_entered.grid(column = 0, row = 1)
blocks_entered.focus()

calculate = ttk.Button(window, text = "Calculate!", command = click_me)
calculate.grid(column = 0, row = 2)

window.mainloop()

        
