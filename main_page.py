import tkinter as tk
from tkinter import ttk


def cryptography_page():

    def encryption_function():
        pass

    def decryption_function():
        pass

    window = tk.Tk()
    window.geometry("1000x600")
    window.title("")

    encryption_var = tk.StringVar()
    decryption_var = tk.StringVar()

    encryption_frame = ttk.Frame(window)
    encryption_entry = ttk.Entry(encryption_frame, textvariable=encryption_var)
    encryption_button = ttk.Button(encryption_frame, text="encrypt", command=encryption_function)

    decryption_frame = ttk.Frame(window)
    decryption_entry = ttk.Entry(decryption_frame, textvariable=decryption_var)
    decryption_button = ttk.Button(decryption_frame, text="decrypt", command=decryption_function)

    window.columnconfigure((0, 1, 2), weight=1, uniform="a")
    window.rowconfigure((0, 1), weight=1, uniform="a")
    encryption_frame.columnconfigure((0, 1, 2), weight=1, uniform="a")
    decryption_frame.columnconfigure((0, 1, 2), weight=1, uniform="a")

    encryption_frame.grid(column=0, row=0, columnspan=3)
    encryption_entry.grid(column=1)

    window.mainloop()
