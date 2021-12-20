from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=("Arial", 12), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Choose Category:", font=("Arial", 18))
        # Whenever we add an image or we add something to the canvas, we always have to provide a position
        # as the first two arguments.
        # We use width so that the text fits in the card
        self.canvas.grid(column=0, row=2, columnspan=2, padx=20, pady=20)

        self.true_pic = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_pic, borderwidth=0, command=self.is_true)
        self.true_button.grid(column=0, row=3, padx=10, pady=10)

        self.false_pic = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_pic, borderwidth=0, command=self.is_false)
        self.false_button.grid(column=1, row=3, padx=10, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            # itemconfig changes the item, here, question_text\
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've completed the quiz. \n\n"
                                      f"Your final score was: {self.quiz.score}/{self.quiz.question_number}.",
                                   font=("Arial", 16)
                                   )
    def is_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def is_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
