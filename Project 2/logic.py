from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from gui import *
from MDL_ChatBotManager import *


class Controller(View):
    def __init__(self) -> None:
        """
        Method to initialize logic and connect logic and gui
        """
        super().__init__()
        super().setupUI()
        
        systemRole = "You are helpgul assistant. You must answer the question as short as possible because text box that you will use is very small so if you answer too long, it cannot be displayed. Please answer user's question less than 100 words."
        self.chatbot = ChatBotManager(systemRole=systemRole)
        self.button_submit.clicked.connect(self.submit)
        self.button_clear_memory.clicked.connect(self.clear_memory)
        self.button_attach_image.clicked.connect(self.attach_image)
        
        self.imagePath = None
    
    def submit(self) -> None:
        """
        Method to send query to chatgpt and display its result
        """
        prompt = self.input_prompt.toPlainText()
        self.label_your_question.setText(prompt)
        self.input_prompt.setPlainText("")
        
        self.chatbot.setAPIKey(self.input_apiKey.text())
        
        if self.imagePath == None:
            reply = self.chatbot.ask(prompt=prompt)
        else:
            reply = self.chatbot.askWithImage(imagePath=self.imagePath, prompt=prompt)
        self.label_gpt_answer.setText(reply)
        
        self.imagePath = None
            
    def clear_memory(self) -> None:
        """
        Method to delete chat history
        """
        self.chatbot.forget()
        self.chatbot.clear()
        
        self.label_your_question.setText("")
        self.label_gpt_answer.setText("")
        self.attached_picure.setPixmap(QPixmap())
        self.imagePath = None
        
    def attach_image(self) -> None:
        """
        Method to resister a image to query
        """
        self.imagePath, _ = QFileDialog.getOpenFileName(self, 'Single File',  '/', '*.jpg')
        self.attached_picure.setPixmap(QPixmap(self.imagePath))