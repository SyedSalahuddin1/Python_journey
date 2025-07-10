from tkinter import *

import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Arabic_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# print(to_learn)


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["Arabic"])
    canvas.itemconfig(card_title, text="Arabic", fill="black")
    canvas.itemconfig(card_word, text=current_card["Arabic"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    # print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0, highlightbackground="White")
card_front_image = PhotoImage(width=800, height=526, file="images/card_front.png")
card_back_image = PhotoImage(width=800, height=526, file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Times New Roman", 40, "italic bold"))
card_word = canvas.create_text(400, 263, text="", font=("Times New Roman", 40, "italic bold"))
canvas.grid(row=0, column=0, columnspan=2)


# back_image = PhotoImage(file="card_back.png")
# canvas.create_image(250, 250, image=back_image)
# canvas.grid(row=0, column=0)


check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, bg="Green", highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, bg="Red", highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)


next_card()


window.mainloop()
