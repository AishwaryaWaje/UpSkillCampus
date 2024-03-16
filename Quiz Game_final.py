import tkinter as tk
from tkinter import messagebox
import random

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

def read_questions(file_path):
    questions = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            question = Question(data[0], data[1:-1], data[-1])
            questions.append(question)
    return questions

class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        random.shuffle(self.questions)  # Shuffle the questions
        self.score = 0
        self.current_question_index = 0

        self.master.title("Quiz Game")

        self.question_label = tk.Label(master, text="")
        self.question_label.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(master, text="", variable=self.radio_var, value=str(i+1))
            self.radio_buttons.append(radio_button)
            radio_button.pack()

        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question.text)

            for i, option in enumerate(question.options):
                self.radio_buttons[i].config(text=option)
                self.radio_buttons[i].deselect()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            user_answer = self.radio_var.get()
            correct_answer = str(self.questions[self.current_question_index].options.index(
                self.questions[self.current_question_index].correct_answer) + 1)

            if user_answer == correct_answer:
                self.score += 1

            self.current_question_index += 1
            self.load_question()

        else:
            self.show_result()

    def show_result(self):
        result_message = f"Your final score is: {self.score}/{len(self.questions)}"
        messagebox.showinfo("Quiz Completed", result_message)
        self.master.destroy()

if __name__ == "__main__":
    file_path = "Questions.txt"  # Replace with your actual file path
    quiz_questions = read_questions(file_path)

    root = tk.Tk()
    app = QuizApp(root, quiz_questions)
    root.mainloop()
