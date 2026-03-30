from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz=quiz_brain

        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label=Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas=Canvas(height=250, width=300, highlightthickness=0, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question=self.canvas.create_text(150,125, width=280, text="question",
                                              font=("Arial",20,"italic"), fill=THEME_COLOR)

        right_image=PhotoImage(file="images/true.png")
        self.right_button=Button(image=right_image, highlightthickness=0, command=self.answer_true)
        self.right_button.grid(row=2, column=0)

        wrong_image=PhotoImage(file="images/false.png")
        self.wrong_button=Button(image=wrong_image, highlightthickness=0, command=self.answer_false)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"You've reached the end of the quiz!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.score_label.config(font=("Arial",25, "bold"))
            self.score_label.grid(row=0, column=0, columnspan=2)
    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.canvas.config(bg="green" * is_right + "red" * (1 - is_right))
        self.window.after(1000,self.get_next_question)