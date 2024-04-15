import tkinter as tk
from tkinter import ttk
from functions import handle_invalid_email, handle_invalid_password
from main_page import cryptography_page
import json


def sign_up():
    def button_function():
        account_taken = False
        with open("passwords.json", "r") as file:
            contents = json.load(file)
            for i in range((len(contents["accounts"]))):
                if contents["accounts"][i]["username"] == username.get():
                    error_label["text"] = "username taken"
                    account_taken = True
                    break
                elif contents["accounts"][i]["email"] == email.get():
                    error_label["text"] = "email already in use"
                    account_taken = True
                    break
        if email.get() == "" or password.get() == "" or username.get() == "":
            error_label["text"] = "empty space"
        elif handle_invalid_email(email.get()) == "invalid":
            error_label["text"] = "invalid email"
        elif handle_invalid_password(password.get()) == "too large":
            error_label["text"] = "password must be less than 20 characters"
        elif handle_invalid_password(password.get()) == "too small":
            error_label["text"] = "password must be more than 3 characters"
        elif handle_invalid_password(password.get()) == "no special chars":
            error_label["text"] = "password must include one of these special characters : \n            !£$%^&*()_-+={[]}@'~#:;><,.?/|`¬"
        elif account_taken == False:
            with open("passwords.json", "r") as file:
                content = json.load(file)
                print(content)

            content["accounts"].append({"email": email.get(),
                                        "username": username.get(),
                                        "password": password.get()})
            with open("passwords.json", "w") as file:
                json.dump(content, file, indent=4)
            window.destroy()
            sign_in()

    def switch_page_function():
        window.destroy()
        sign_in()

    window = tk.Tk()
    window.title("Sign Up")
    window.geometry("1000x600")
    window.resizable(False, False)

    username = tk.StringVar(value=None)
    password = tk.StringVar(value=None)
    email = tk.StringVar(value=None)

    sign_up_label = ttk.Label(window, text="Create an account", font=3)
    email_label = ttk.Label(window, text="email")
    email_entry = ttk.Entry(window, textvariable=email)
    username_label = ttk.Label(window, text="username")
    username_entry = ttk.Entry(window, textvariable=username)
    password_label = ttk.Label(window, text="password")
    password_entry = ttk.Entry(window, textvariable=password)
    sign_up_button = ttk.Button(window, text="sign up", command=button_function)
    already_have_an_account_label = ttk.Label(window, text="already have an account?")
    sign_in_button = ttk.Button(window, text="sign in", command=switch_page_function)
    error_label = ttk.Label(window, text="")

    window.columnconfigure((0, 1, 3, 4), weight=1, uniform="a")
    window.columnconfigure(2, weight=2, uniform="a")
    window.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1, uniform="a")

    sign_up_label.grid(column=2, row=0, sticky="s")
    email_label.grid(column=2, row=1, sticky="w")
    email_entry.grid(column=2, row=1, sticky="sew")
    username_label.grid(column=2, row=2, sticky="w")
    username_entry.grid(column=2, row=2, sticky="sew")
    password_label.grid(column=2, row=3, sticky="w")
    password_entry.grid(column=2, row=3, sticky="sew")
    sign_up_button.grid(column=2, row=4, sticky="esw")
    already_have_an_account_label.grid(column=2, row=5)
    sign_in_button.grid(column=2, row=5, sticky="esw")
    error_label.grid(column=2, row=6)

    window.mainloop()


def sign_in():
    def sign_in_button_function():
        with open("passwords.json", "r") as file:
            contents = json.load(file)
            for i in range((len(contents["accounts"]))):
                if (contents["accounts"][i]["email"] == username_email.get() or contents["accounts"][i]["username"] == username_email.get()) and contents["accounts"][i]["password"] == password.get():
                    window.destroy()
                    cryptography_page()
                    break
            else:
                error_label["text"] = "username, email or password invalid"

    def create_account_button_function():
        window.destroy()
        sign_up()

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
    password_entry = ttk.Entry(window, textvariable=password, show="*")
    sign_in_button = ttk.Button(window, text="sign in", command=sign_in_button_function)
    dont_have_an_account_label = ttk.Label(window, text="don't have an account?")
    create_account_button = ttk.Button(window, text="create an account", command=create_account_button_function)

    window.columnconfigure((0, 1, 3, 4), weight=1, uniform="a")
    window.columnconfigure(2, weight=2, uniform="a")
    window.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform="a")

    sign_up_label.grid(column=2, row=0, sticky="s")
    username_label.grid(column=2, row=1, sticky="w")
    username_entry.grid(column=2, row=1, sticky="sew")
    password_label.grid(column=2, row=2, sticky="w")
    password_entry.grid(column=2, row=2, sticky="sew")
    sign_in_button.grid(column=2, row=3, sticky="sew")
    dont_have_an_account_label.grid(column=2, row=4)
    create_account_button.grid(column=2, row=4, sticky="sew")
    error_label.grid(column=2, row=5)

    window.mainloop()


sign_in()