from gui import *
from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.voter_choices = {}
        self.john_votes = 0
        self.jane_votes = 0
        self.submit_button.clicked.connect(lambda: self.submit())
        self.results_button.clicked.connect(self.display_results)

    def submit(self):
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
            else:
                QMessageBox.warning(self, "Warning", "Please select a candidate.")
        else:
            self.detail_label.setText("<font color='red'>Please enter your Voter ID.</font>")

    def display_results(self):
        self.detail_label.setText(f"John: {self.john_votes} votes\nJane: {self.jane_votes} votes")
        font = self.detail_label.font()
        font.setPointSize(15)
        self.detail_label.setFont(font)

