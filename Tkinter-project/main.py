from tkinter import *


def button_clicked():
    print("button got clicked.")
    # label1.config(text="I got clicked🤩")
    my_text = input1.get()
    my_label.config(text=my_text)


window = Tk()

window.title("My First GUI Program")
window.minsize(400, 300)
window.config(padx=20, pady=20)

my_label = Label(text="I am a Label", font=("Times New Roman", 24, "italic"))
my_label.pack(side="top")
my_label.grid(column=0, row=0)


my_label["text"] = "New Text"
my_label.config(text="New Text")


input1 = Entry()
print(input1.get())
input1.grid(column=0, row=1)
button = Button(text="Click Me", command=button_clicked)
button.grid(column=0, row=2)

text = Text(height=5, width=15)
text.insert(END, "Be Consistent")
text.grid(column=3, row=0)

window.mainloop()

