import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("1000x1000")

var1 = tk.IntVar()


radio1 = ttk.Radiobutton(window, variable=var1, value=2)
radio2 = ttk.Radiobutton(window, variable=var1, value=1, command=lambda: print("hello"))

radio1.pack()
radio2.pack()

window.mainloop()

