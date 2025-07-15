from tkinter import *

THEME_COLOR = "#375362"
from quiz_brain import QuizBrain


class QuizInterface:
    #
    # def is_false(self):
    #     pass

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler App")
        # self.window.minsize(350, 375)
        self.window.config(padx=20, pady=20)
        self.window.config(bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Some Question text",
            fill=THEME_COLOR,
            width=280,
            font=("Times New Roman", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=right_image, bg=THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(column=0, row=2)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, bg=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2)

        # self.true_pressed()

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.Bye")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.canvas.config(bg="white")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


