from tkinter import *
import requests

# quotes = requests.get(url="https://api.kanye.rest/")
window = Tk()
window.config(padx=50, pady=50)
window.title("Kanye Says")


def get_quote():
    quotes = requests.get(url="https://api.kanye.rest/")
    quotes.raise_for_status()
    data = quotes.json()
    quote = data["quote"]
    print(quote)
    canvas.itemconfig(quote_text, text=quote)


canvas = Canvas(width=300, height=414)
background_image = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_image)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250,
                                font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)


kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, highlightbackground="black")
kanye_button.grid(row=1, column=0)

window.mainloop()
