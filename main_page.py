import tkinter as tk
from tkinter import ttk
from functions import handle_decryption, handle_encryption


def general_purpose_page():

    def encryption_function():
        encryption_output["text"] = handle_encryption(encryption_var.get())

    def decryption_function():
        decryption_output["text"] = handle_decryption(decryption_var.get())

    window = tk.Tk()
    window.geometry("1000x600")
    window.title("")

    # creating columns and rows for the window

    window.columnconfigure(0, weight=1, uniform="a")
    window.columnconfigure(1, weight=4, uniform="a")
    window.rowconfigure(0, weight=1, uniform="a")

    # declaring tk variables for nav bar

    nav_bar_var = tk.IntVar()

    # creating nav bar frames and widgets

    nav_bar_frame = tk.Frame(window, width=100, height=100, bg="yellow")
    main_page_radio_button = ttk.Radiobutton(nav_bar_frame, text="main page", variable=nav_bar_var, value=1, command=lambda: main_page_frame.tkraise())
    cryptography_page_radio_button = ttk.Radiobutton(nav_bar_frame, text="cryptography", variable=nav_bar_var, value=2, command=lambda: cryptography_frame.tkraise())

    # creating columns and rows for nav bar frame

    nav_bar_frame.columnconfigure(0, weight=1, uniform="a")
    nav_bar_frame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="a")

    # positioning radio buttons onto nav bar frame

    main_page_radio_button.grid(column=0, row=0)
    cryptography_page_radio_button.grid(column=0, row=0, sticky="s")

    # creating main page frames and widgets

    main_page_frame = tk.Frame(window, width=100, height=100, bg="purple")
    main_page_label = ttk.Label(main_page_frame, text="main page", font=2)

    # creating columns and rows for main page

    main_page_frame.columnconfigure(0, weight=1, uniform="a")
    main_page_frame.rowconfigure(0, weight=1, uniform="a")

    # positioning widgets onto main page

    main_page_label.grid(column=0, row=0)

    # declaring tk variables for cryptography page

    encryption_var = tk.StringVar()
    decryption_var = tk.StringVar()
    crypt_radio_button_var = tk.IntVar()
    nav_radio_button_var = tk.IntVar()

    # creating cryptography page frames and widgets

    cryptography_frame = tk.Frame(window, width=100, height=100, bg="green")

    encryption_frame = tk.Frame(cryptography_frame, width=100, height=100, bg="red")
    encryption_title = ttk.Label(encryption_frame, text="Encrypt", font=3)
    encryption_entry = ttk.Entry(encryption_frame, textvariable=encryption_var)
    encryption_button = ttk.Button(encryption_frame, text="encrypt", command=encryption_function)
    encryption_output = ttk.Label(encryption_frame)

    decryption_frame = tk.Frame(cryptography_frame, width=100, height=100)
    decryption_title = ttk.Label(decryption_frame, text="Decrypt", font=3)
    decryption_entry = ttk.Entry(decryption_frame, textvariable=decryption_var)
    decryption_button = ttk.Button(decryption_frame, text="decrypt", command=decryption_function)
    decryption_output = ttk.Label(decryption_frame)

    crypt_radio_button_frame = tk.Frame(cryptography_frame, width=100, height=100)
    encryption_radio_button = ttk.Radiobutton(crypt_radio_button_frame, text="encryption", variable=crypt_radio_button_var, value=1, command=lambda: encryption_frame.tkraise())
    decryption_radio_button = ttk.Radiobutton(crypt_radio_button_frame, text="decryption", variable=crypt_radio_button_var, value=2, command=lambda: decryption_frame.tkraise())

    # creating columns and rows for frames

    cryptography_frame.columnconfigure(0, weight=1, uniform="a")
    cryptography_frame.columnconfigure(1, weight=2, uniform="a")
    cryptography_frame.rowconfigure(0, weight=1, uniform="a")

    encryption_frame.columnconfigure(0, weight=1, uniform="a")
    encryption_frame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="a")

    decryption_frame.columnconfigure(0, weight=1, uniform="a")
    decryption_frame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="a")

    crypt_radio_button_frame.columnconfigure(0, weight=1, uniform="a")
    crypt_radio_button_frame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="a")

    # positioning the encryption frame onto cryptography frame

    encryption_frame.grid(column=1, row=0, sticky="nsew")
    encryption_title.grid(column=0, row=0, sticky="s")
    encryption_entry.grid(column=0)
    encryption_button.grid(column=0, row=2, sticky="n")
    encryption_output.grid(column=0, row=2, sticky="s")

    # positioning the decryption frame onto cryptography frame

    decryption_frame.grid(column=1, row=0, sticky="nsew")
    decryption_title.grid(column=0, row=0, sticky="s")
    decryption_entry.grid(column=0)
    decryption_button.grid(column=0, row=2, sticky="n")
    decryption_output.grid(column=0, row=2, sticky="s")

    # positioning cryptography radio button frame onto cryptography frame

    crypt_radio_button_frame.grid(column=0, row=0, sticky="nsew")
    encryption_radio_button.grid(column=0, row=0)
    decryption_radio_button.grid(column=0, row=0, sticky="s")

    # placing each purpose frame

    nav_bar_frame.grid(column=0, sticky="nsew")
    main_page_frame.grid(column=1, row=0, columnspan=2, sticky="nsew")
    cryptography_frame.grid(column=1, row=0, columnspan=2, sticky="nsew")

    # window mainloop

    window.mainloop()


general_purpose_page()
