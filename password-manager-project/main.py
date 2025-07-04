from tkinter import *
from tkinter import messagebox
YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                           f"\nPassword: {password} \nIs it ok to save?")
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            web_entry.delete(0, END)
            password_entry.delete(0, END)


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

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, sticky="w", columnspan=2)
email_entry.insert(0, "salah@gmail.com")

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1, sticky="w", columnspan=2)

gen_pass = Button(text="Generate Password")
gen_pass.grid(row=3, column=2, sticky="w")

add_butt = Button(text="ADD", width=36, command=save)
add_butt.grid(row=4, column=1, columnspan=2, sticky="w")

window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=0)


window.mainloop()
