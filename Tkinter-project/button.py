from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(200, 100)
window.config(padx=20, pady=20)

# Frame to hold circles and title
title_frame = Frame(window)
title_frame.pack()

# Function to draw a circle


def draw_circle(parent, color):
    canvas = Canvas(parent, width=20, height=20, highlightthickness=0)
    canvas.create_oval(2, 2, 18, 18, fill=color, outline="")
    canvas.pack(side="left", padx=3)

# Draw 3 different colored circles


draw_circle(title_frame, "red")
draw_circle(title_frame, "green")
draw_circle(title_frame, "blue")

# Text label
title_label = Label(title_frame, text="Mile to Km Converter", fg="black", font=("Arial", 14, "bold"))
title_label.pack(side="left", padx=10)

window.mainloop()
