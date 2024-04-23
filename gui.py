from tkinter import *
import logic


class Gui:
    def __init__(self, window):
        self.window = window.configure(background='White')

        self.frame_zero = Frame(self.window)
        self.voting_label = Label(self.frame_zero, text='Voting Application', font=('Arial', 50))
        self.voting_label.pack()
        self.frame_zero.pack(anchor='n')


        self.frame_one = Frame(self.window)
        self.name_label = Label(self.frame_one, text='ID', bg='White', fg='black', font=("Arial", 25))
        self.input_name = Entry(self.frame_one)
        self.name_label.pack(side='left')
        self.input_name.pack(side='left', padx=5)
        self.frame_one.pack(anchor='w', padx=10, pady=10)


        self.frame_two = Frame(self.window)
        self.candidate_label = Label(self.frame_two, text='Candidates', bg='White', fg='black', font=("Arial", 25))
        self.candidate_label.pack(side='left')
        self.frame_two.pack()

        self.frame_three = Frame(self.window, background='Black', bd='100')
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.radio_jane = Radiobutton(self.frame_three, text='Jane', variable=self.radio_answer, value=1,
                                      font=("Arial", 25))
        self.radio_John = Radiobutton(self.frame_three, text='John', variable=self.radio_answer, value=2,
                                      font=("Arial", 25))
        self.radio_jane.pack(side='bottom')
        self.radio_John.pack(side='bottom')
        self.frame_three.pack()

        self.frame_four = Frame(self.window, background='Black', bd='20')
        self.button_save = Button(self.frame_four, text='Save')  # command=self.submit)
        self.label_fill = Label(self.frame_four, text='Please fill out all fields', fg='black')
        self.button_save.pack(side='top')
        self.label_fill.pack(side='bottom')
        self.frame_four.pack(side='bottom', padx=10, pady=10)
        self.frame_four.pack()
