from tkinter import *
import logic


class Gui:
    def __init__(self, window):
        self.window = window.configure(background='White')
        self.frame_one = Frame(self.window)
        self.name_label = Label(self.frame_one, text='ID', bg='White', fg='black', font=("Arial", 25))
        self.input_name = Entry(self.frame_one)
        self.name_label.pack(side='left')
        self.input_name.pack(side='left', padx=5)
        self.frame_one.pack(anchor='w', padx=10, pady=10)

        self.frame_two = Frame(self.window)
        self.age_label = Label(self.frame_two, text='Pin', bg='White', fg='black', font=("Arial", 25))
        self.age_input = Entry(self.frame_two)
        self.age_label.pack(side='left')
        self.age_input.pack(side='left', padx=5)
        self.frame_two.pack(anchor='w', padx=10, pady=10)

        self.frame_three = Frame(self.window)
        self.candidate_label = Label(self.frame_three, text='Candidates', bg='White', fg='black', font=("Arial", 25))
        self.candidate_label.pack(side='left')
        self.frame_three.pack()

        self.frame_four = Frame(self.window)
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.radio_jane = Radiobutton(self.frame_four, text='Jane', variable=self.radio_answer, value=1, font=("Arial", 25))
        self.radio_John = Radiobutton(self.frame_four, text='John', variable=self.radio_answer, value=2, font=("Arial", 25))
        self.radio_jane.pack(side='bottom')
        self.radio_John.pack(side='bottom')
        self.frame_four.pack()
