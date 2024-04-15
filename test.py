import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("1000x1000")
frame = tk.Frame(bg="red", width=200, height=200)
entry = ttk.Entry(frame)
window.columnconfigure((0, 1, 2), weight=1, uniform="a")
frame.grid(column=1)
entry.grid(column=0)
window.mainloop()
