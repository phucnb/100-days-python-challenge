from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')
WIDTH = 300
HEIGHT = 250

class QuizInterface:

    def __init__(self, quiz: QuizBrain) -> None:
        self.window = Tk()
        self.window.title()
        self.window.config(bg=THEME_COLOR)
        self.quiz = quiz
        
        self.score = Label(self.window, text="Score: 0", bg=THEME_COLOR, font=FONT)
        self.score.grid(column=1, row=0, padx=20, pady=20)
        
        self.canvas = Canvas(width=WIDTH, height=HEIGHT, bg='white')
        self.question_text = self.canvas.create_text(WIDTH/2, HEIGHT/2, width=WIDTH-20, text="", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        false_img = PhotoImage(file='images/false.png')
        true_img = PhotoImage(file='images/true.png')

        self.false_btn = Button(self.window, image=false_img, border=0, command=self.false_pressed)
        self.false_btn.grid(column=0, row=2, padx=20, pady=20)
        self.true_btn = Button(self.window, image=true_img, border=0, command=self.true_pressed)
        self.true_btn.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text, fill=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.question_text, text="No more questions", fill=THEME_COLOR)
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')



    def true_pressed(self):
        correct = self.quiz.check_answer(user_answer='true')
        self.give_feedback(correct)
        self.update_score()
    
    def false_pressed(self):
        correct = self.quiz.check_answer(user_answer='false')
        self.give_feedback(correct)
        self.update_score()

    def update_score(self):
        score = self.quiz.score
        self.score['text'] = f"Score: {score}"

    def give_feedback(self, correct: bool):
        if correct:
            self.canvas.config(bg='green')
            self.canvas.itemconfig(self.question_text, fill='white')
        else:
            self.canvas.config(bg='red')
            self.canvas.itemconfig(self.question_text, fill='white')
        self.window.after(1500, self.get_next_question)
