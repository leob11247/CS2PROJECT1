from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *

class View(QWidget):
    def __init__(self) -> None:
        """
        Method to initialize GUI
        """
        super().__init__()
        
    def setupUI(self) -> None:
        """
        Method to initialize GUI
        """
        self.setFixedSize(600, 600)
        self.setWindowTitle('Talk with ChatGPT')
         
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        self.label_apiKey = QLabel('API key', alignment=Qt.AlignmentFlag.AlignLeading)
        self.label_apiKey.setFixedWidth(100)
        self.input_apiKey = QLineEdit()
        self.input_apiKey.setFixedWidth(450)
        HBox_api = QHBoxLayout()
        HBox_api.addWidget(self.label_apiKey)
        HBox_api.addWidget(self.input_apiKey)
        HBox_api.addStretch(1)
        layout.addLayout(HBox_api)
        
        self.label_you = QLabel('You', alignment=Qt.AlignmentFlag.AlignLeading)
        self.label_you.setFixedWidth(100)
        self.label_your_question = QLabel('', alignment=Qt.AlignmentFlag.AlignLeading)
        self.label_your_question.setFixedWidth(450)
        self.label_your_question.setWordWrap(True)
        HBox_you = QHBoxLayout()
        HBox_you.addWidget(self.label_you)
        HBox_you.addWidget(self.label_your_question)
        HBox_you.addStretch(1)
        layout.addLayout(HBox_you)
        
        self.label_gpt = QLabel('ChatGPT', alignment=Qt.AlignmentFlag.AlignLeading)
        self.label_gpt.setFixedWidth(100)
        self.label_gpt_answer = QLabel('', alignment=Qt.AlignmentFlag.AlignLeading)
        self.label_gpt_answer.setFixedWidth(450)
        self.label_gpt_answer.setWordWrap(True)
        HBox_gpt = QHBoxLayout()
        HBox_gpt.addWidget(self.label_gpt)
        HBox_gpt.addWidget(self.label_gpt_answer)
        layout.addLayout(HBox_gpt)
        
        layout.addStretch(1)
        
        self.attached_picure = QLabel()
        self.attached_picure.setFixedHeight(200)
        layout.addWidget(self.attached_picure)
        
        HBox_question_form = QHBoxLayout()
        self.input_prompt = QPlainTextEdit()
        self.input_prompt.setFixedHeight(70)
        self.button_submit = QPushButton('Submit')
        self.button_submit.setFixedHeight(70)
        self.button_clear_memory = QPushButton('Clear\nmemory')
        self.button_clear_memory.setFixedHeight(70)
        self.button_attach_image = QPushButton('attach\nimage')
        self.button_attach_image.setFixedHeight(70)
        HBox_question_form.addWidget(self.input_prompt)
        HBox_question_form.addWidget(self.button_submit)
        HBox_question_form.addWidget(self.button_attach_image)
        HBox_question_form.addWidget(self.button_clear_memory)
        layout.addLayout(HBox_question_form)
        
        self.setLayout(layout)
        