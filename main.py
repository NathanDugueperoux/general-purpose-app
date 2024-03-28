import tkinter as tk
from tkinter import ttk
from functions import handle_invalid_email, handle_invalid_password


def sign_up():
    def button_function():
        if email.get() == "" or password.get() == "" or username.get() == "":
            error_label["text"] = "empty space"
        elif handle_invalid_email(email.get()) == "invalid":
            error_label["text"] = "invalid email"
        elif handle_invalid_password(password.get()) == "too large":
            error_label["text"] = "password must be less than 20 characters"
        elif handle_invalid_password(password.get()) == "too small":
            error_label["text"] = "password must be more than 3 characters"
        elif handle_invalid_password(password.get()) == "no special chars":
            error_label["text"] = "password must include one of these special characters: !£$%^&*()_-+={[]}@'~#:;><,.?/|`¬"
        else:
            with open("passwords.txt", "w") as file:
                file.write(f"{username.get()}\n{password.get()}\n{email.get()}")
            username_label["text"] = "username"
            window.destroy()
            sign_in()

    window = tk.Tk()
    window.title("Sign Up")
    window.geometry("1000x600")
    window.resizable(False, False)

    username = tk.StringVar(value=None)
    password = tk.StringVar(value=None)
    email = tk.StringVar(value=None)

    error_label = ttk.Label(window, text="")
    sign_up_label = ttk.Label(window, text="Sign Up", font=3)
    email_label = ttk.Label(window, text="email")
    email_entry = ttk.Entry(window, textvariable=email)
    username_label = ttk.Label(window, text="username")
    username_entry = ttk.Entry(window, textvariable=username)
    password_label = ttk.Label(window, text="password")
    password_entry = ttk.Entry(window, textvariable=password)
    button_entry = ttk.Button(window, text="sign up", command=button_function)

    window.columnconfigure((0, 1, 3, 4), weight=1, uniform="a")
    window.columnconfigure(2, weight=2, uniform="a")
    window.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="a")

    sign_up_label.grid(column=2, row=0, sticky="s")
    email_label.grid(column=2, row=1, sticky="w")
    email_entry.grid(column=2, row=1, sticky="sew")
    username_label.grid(column=2, row=2, sticky="w")
    username_entry.grid(column=2, row=2, sticky="sew")
    password_label.grid(column=2, row=3, sticky="w")
    password_entry.grid(column=2, row=3, sticky="sew")
    button_entry.grid(column=2, row=4, sticky="esw")
    error_label.grid(column=2, row=5)

    window.mainloop()


def sign_in():

    def button_function():
        with open("passwords.txt", "r") as file:
            content = file.readlines()
            if (f"{username_email.get()}\n" == content[0] or f"{username_email.get()}" == content[2]) and f"{password.get()}\n" == content[1]:
                window.destroy()
            else:
                error_label["text"] = "wrong email, username or password"

    window = tk.Tk()

    window.title("Sign In")
    window.geometry("1000x500")
    window.resizable(False, False)

    username_email = tk.StringVar(value=None)
    password = tk.StringVar(value=None)

    error_label = ttk.Label(window, text="")
    sign_up_label = ttk.Label(window, text="Sign In", font=3)
    username_label = ttk.Label(window, text="username or email")
    password_label = ttk.Label(window, text="password")
    username_entry = ttk.Entry(window, textvariable=username_email)
    password_entry = ttk.Entry(window, textvariable=password)
    button_entry = ttk.Button(window, text="sign up", command=button_function)

    window.columnconfigure((0, 1, 3, 4), weight=1, uniform="a")
    window.columnconfigure(2, weight=2, uniform="a")
    window.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="a")

    sign_up_label.grid(column=2, row=0, sticky="s")
    username_label.grid(column=2, row=1, sticky="w")
    username_entry.grid(column=2, row=1, sticky="sew")
    password_label.grid(column=2, row=2, sticky="w")
    password_entry.grid(column=2, row=2, sticky="sew")
    button_entry.grid(column=2, row=3, sticky="esw")
    error_label.grid(column=2, row=4)

    window.mainloop()


with open("passwords.txt", "r") as file:
    if file.read() == "":
        sign_up()
    else:
        sign_in()
