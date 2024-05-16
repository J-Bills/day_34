from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self,quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 100, text="Quiz question", width=250, font=("Arial", 20, "italic"), fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=20)
        
        self.score_label = Label(text=f"Score:{self.score}", fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        
        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true, pady=10, fg='green')
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false, pady=10, fg='red')
        self.false_button.grid(row=2, column=1)
        
        self.question = self.get_next_question()
                
        self.window.mainloop()
        
    def get_next_question(self):
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question.text)
        return question
            
    def answer_true(self):
        usr_answer = 'True'
        if self.quiz.check_answer(usr_answer):
            self.score += 1
            self.score_label.config(text=f"Score:{self.score}")
        try:
            self.get_next_question()
        except IndexError:
            self.true_button.config(state='disable')
            self.canvas.itemconfig(self.question_text, text=f"Final Score{self.score} / 10")
    
    def answer_false(self):
        usr_answer = 'False'
        if self.quiz.check_answer(usr_answer):
            self.score += 1
            self.score_label.config(text=f"Score:{self.score}")
        try:
            self.get_next_question()
        except IndexError:
            self.false_button.config(state='disable')
            self.canvas.itemconfig(self.question_text, text=f"Final Score{self.score} / 10")
            