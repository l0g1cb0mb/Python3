import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title("Pyramid maker")
window_width = 250
window_height = 100
window.geometry(str(window_width)+"x"+str(window_height))
window.rowconfigure(0, weight = 1)
window.columnconfigure(0, weight = 1)

question = ttk.Label(window, text = "How many blocks do you have?").grid(column = 0, row = 0)

def close(event):
    window.withdraw()
    exit(0)

def get_user_input():
    blocks_entered = ttk.Entry(window, width = 12, textvariable = blocks)
    blocks_entered.grid(column = 0, row = 1, sticky = "nsew")
    blocks_entered.focus()

def click_me(event = 0):
    height = 0
    try:
        tmp = int(blocks.get())
    except ValueError as err:
        messagebox.showinfo("Pyramid maker", "The parameter type must be int")
        blocks.set("")
        tmp = 0
        get_user_input()
    except:
        messagebox.showinfo("Pyramid maker", "Unexpected error occured! The program will close")
        window.withdraw()
        exit(0)
    else:
        while blocks:
            if ((height + 1) <= tmp):
                tmp -= (height + 1)
                height += 1
            else:
                break;

        messagebox.showinfo("Pyramid maker", "You have " + blocks.get() + " blocks and you can make a pyramid with a height of " + str(height))
        blocks.set("")
        get_user_input()
    

window.bind("<Return>", click_me)
window.bind("<q>", close)

blocks = tk.StringVar()
get_user_input()

calculate = ttk.Button(window, text = "Calculate!", command = click_me)
calculate.grid(column = 0, row = 2)

window.mainloop()

        
