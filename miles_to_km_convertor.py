from tkinter import *


def calculate():
    miles = float(input_taker.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Convertor")
window.minsize(150, 100)
window.config(padx=20, pady=20)

label1 = Label(text="is equal to", font=("Times New Roman", 15))
label1.grid(column=0, row=1)

label2 = Label(text="Miles", font=("Times New Roman", 15))
label2.grid(column=2, row=0)

label3 = Label(text="Km", font=("Times New Roman", 15))
label3.grid(column=2, row=1)

input_taker = Entry(width=7)
print(input_taker.get())
input_taker.grid(column=1, row=0)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
