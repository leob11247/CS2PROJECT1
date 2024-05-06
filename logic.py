from gui import *
from PyQt6.QtWidgets import *
from gui import *
import csv
import os


class Logic(QMainWindow, Ui_MainWindow):
    """
    Class responsible for the logic and UI interaction of the voting application.
    """
    def __init__(self):
        """
        Initializes the voting application.
        Gets rid of the previous votes.csv file.
        """
        super().__init__()
        self.setupUi(self)
        self.voter_choices = {}
        self.john_votes = 0
        self.jane_votes = 0
        self.submit_button.clicked.connect(lambda: self.submit())
        if os.path.exists('votes.csv'):
            os.remove('votes.csv')
        self.results_button.clicked.connect(self.display_results)


    def submit(self) -> None:
        """
        Handles the submission of a vote, adds it to the csv file and handles errors.
        """
        voter_id = self.id_input.text()
        candidate = ""
        if self.Joh_Button.isChecked():
            candidate = "John"
        elif self.Jane_radio.isChecked():
            candidate = "Jane"

        if voter_id:
            if candidate:
                if voter_id in self.voter_choices:
                    self.detail_label.setText("<font color='red'>You have already voted!</font>")
                else:
                    self.voter_choices[voter_id] = candidate
                    self.detail_label.setText(f"Vote submitted for {candidate}!")

                    if candidate == "John":
                        self.john_votes += 1
                    elif candidate == "Jane":
                        self.jane_votes += 1

                    with open('votes.csv', 'a', newline='') as csvfile:
                        vote_writer = csv.writer(csvfile)
                        vote_writer.writerow([voter_id, candidate])

                    self.id_input.clear()
                    self.Candidate_Group.setExclusive(False)
                    self.Joh_Button.setChecked(False)
                    self.Jane_radio.setChecked(False)
                    self.Candidate_Group.setExclusive(True)
            else:
                QMessageBox.warning(self, "Warning", "Please select a candidate.")
        else:
            self.detail_label.setText("<font color='red'>Please enter your Voter ID.</font>")

    def display_results(self) -> None:
        """
        Reads the vote counts from 'votes.csv' and displays the results in a pop-up window.
        Handles cases where the file might be empty or there are read errors.
        """

        try:
            john_votes = 0
            jane_votes = 0

            with open('votes.csv', 'r') as csvfile:
                vote_reader = csv.reader(csvfile)
                for row in vote_reader:
                    if row[1] == 'John':
                        john_votes += 1
                    elif row[1] == 'Jane':
                        jane_votes += 1

            results_text = f"John: {john_votes} votes\nJane: {jane_votes} votes"

            results_window = QMessageBox()
            results_window.setWindowTitle("Voting Results")
            results_window.setText(results_text)
            font = results_window.font()
            font.setPointSize(15)
            results_window.setFont(font)
            results_window.exec()

        except (FileNotFoundError, IndexError):
            QMessageBox.warning(self, "Error", "No results found. Please cast some votes first.")