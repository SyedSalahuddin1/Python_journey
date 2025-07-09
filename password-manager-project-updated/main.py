from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

YELLOW = "#f7f5dd"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

# password_list = []

# for char in range(nr_letters):
#     password_list.append(random.choice(letters))


# for char in range(nr_symbols):
#     password_list += random.choice(symbols)
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# for char in range(nr_numbers):
#     password_list += random.choice(numbers)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure you haven't left any fields empty.")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
        #                                                       f"\nPassword: {password} \nIs it ok to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # data_file.write(f"{website} | {email} | {password}\n")
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message="No Detail found for this query")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=1, highlightbackground="black")
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0, sticky="e")

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, sticky="w", columnspan=2)
web_entry.focus()

search_button = Button(text="Search", width=16, bg="blue", command=find_password)
search_button.grid(row=1, column=2, sticky="w")

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, sticky="w")
email_entry.insert(0, "salah@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky="w", columnspan=2)

gen_pass = Button(text="Generate Password", command=generate_password, width=16, bg="yellow")
gen_pass.grid(row=3, column=2, sticky="w")

add_butt = Button(text="ADD", width=36, command=save)
add_butt.grid(row=4, column=1, columnspan=2, sticky="w")

window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=0)

window.mainloop()
