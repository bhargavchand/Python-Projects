import tarfile
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for item in range(nr_letters)]
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure to enter email and password")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search_info():
    search_string = website_entry.get()
    print(search_string)
    try:
        with open("data.json","r") as json_file:
            load_data = json.load(json_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if search_string in load_data:
            email = load_data[search_string]['email']
            password = load_data[search_string]['password']
            messagebox.showinfo(title=load_data, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search_string} exists.")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.geometry("600x450")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)
# labels
website_label = Label(text="website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# inputs
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, columnspan=1, sticky=W)
website_entry.focus()
email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)
email_entry.insert(0, "test@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, sticky=W)

# button
search_button = Button(text="Search", width=20, command=search_info)
search_button.grid(row=1, column=2)
generate_password = Button(text="Generate Password", width=20, command=generate_password)
generate_password.grid(row=3, column=2, sticky=W)
add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
