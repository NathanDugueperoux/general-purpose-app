import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style


def cryptography_page():

    def encryption_function():
        pass

    def decryption_function():
        pass

    window = tk.Tk()
    window.geometry("1000x600")
    window.title("")

    # declaring tk variables

    encryption_var = tk.StringVar()
    decryption_var = tk.StringVar()
    radio_button_var = tk.IntVar()

    # creating the widgets and frames

    encryption_frame = tk.Frame(window, width=100, height=100)
    encryption_entry = ttk.Entry(encryption_frame, textvariable=encryption_var)
    encryption_button = ttk.Button(encryption_frame, text="encrypt", command=encryption_function)

    decryption_frame = tk.Frame(window, width=100, height=100)
    decryption_entry = ttk.Entry(decryption_frame, textvariable=decryption_var)
    decryption_button = ttk.Button(decryption_frame, text="decrypt", command=decryption_function)

    radio_button_frame = tk.Frame(window, width=100, height=100)
    encryption_radio_button = ttk.Radiobutton(radio_button_frame, text="encryption", variable=radio_button_var, value=1, command=lambda: encryption_frame.tkraise())
    decryption_radio_button = ttk.Radiobutton(radio_button_frame, text="decryption", variable=radio_button_var, value=2, command=lambda: decryption_frame.tkraise())

    # creating columns and rows for the window

    window.columnconfigure(0, weight=1, uniform="a")
    window.columnconfigure((1, 2), weight=2, uniform="a")
    window.rowconfigure(0, weight=1, uniform="a")

    # creating columns and rows for frames

    encryption_frame.columnconfigure(0, weight=1, uniform="a")
    encryption_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")

    decryption_frame.columnconfigure(0, weight=1, uniform="a")
    decryption_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")

    radio_button_frame.columnconfigure(0, weight=1, uniform="a")
    radio_button_frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

    # positioning the encryption frame

    encryption_frame.grid(column=1, row=0, sticky="nsew")
    encryption_entry.grid(column=0, sticky="s")
    encryption_button.grid(column=0, row=1)

    # positioning the decryption frame

    decryption_frame.grid(column=1, row=0, sticky="nesw")
    decryption_entry.grid(column=0, sticky="s")
    decryption_button.grid(column=0, row=1)

    # positioning radio button frame

    radio_button_frame.grid(column=0, row=0, sticky="nesw")
    encryption_radio_button.grid(column=0, row=0, sticky="s")
    decryption_radio_button.grid(column=0, row=0)

    # window mainloop

    window.mainloop()
