from FARM_ChatGPT import *
import csv
import base64
from MDL_ImageEditer import *

class ChatBotManager:
    def __init__(self, systemRole: str='You are helpful assistant.') -> None:
        """
        Method to initialize LLMs (In this case, it's only chatgpt)
        :param systemRole: system role that LLMs will act
        """
        self.chatGPT = ChatGPT()
        self.chatGPT.setModel("gpt-4-turbo")
        self.systemRole = systemRole
        self.chatGPT.setSystemRole(content=self.systemRole)
        self.remember()
        
    def setAPIKey(self, apikey: str) -> None:
        """
        Method to set API key.
        :param apiKey: API key
        """
        self.chatGPT.setAPIKey(apikey)
               
    def clear(self) -> None:
        """
        Method to reset chat history.
        """
        self.chatGPT.clearConversation()
        self.chatGPT.setSystemRole(content=self.systemRole)
        
    def memorize(self, userPrompt: str, reply: str, image: str) -> bool:
        """
        Method to record chat history to csv file.
        :param userPrompt: what user said. (user prompt)
        :param reply: what LLM said. (reply from LLM)
        
        :return: whether the record was successful or not
        """
        try:
            with open('memory.csv', mode='a') as csvfile:
                memory = csv.writer(csvfile)
                memory.writerow(["user", userPrompt, image])
                memory.writerow(["assistant", reply, ""])
            return True
        except Exception as e:
            print(str(e))
            return False
    
    def forget(self) -> bool:
        """
        Method to delete all chat history from csv file.
        
        :return: whether the deletion was successful or not
        """
        try:
            with open('memory.csv', mode='w') as csvfile:
                memory = csv.writer(csvfile)
            return True
        except Exception as e:
            print(str(e))
            return False
        
    def remember(self) -> bool:
        """
        Method to load chat history from csv file.
        
        :return: whether the load was successful or not
        """
        try:
            with open('memory.csv', mode='r') as csvfile:
                memory = csv.reader(csvfile)
                
                for content in memory:
                    if content[2] == "":
                        self.chatGPT.setMessage(content[0], content[1])
                    else:
                        self.chatGPT.setEncordedPicture(content[2], content[1])
                    
            return True    
        except Exception as e:
            print(str(e))
            return False
            
    def ask(self, prompt: str) -> str:
        """
        Method to post request to chatgpt
        
        :param prompt: what user asked to chatgpt
        
        :return: chatgpt's reply
        """
        try:
            self.chatGPT.setMessage(role="user", content=prompt)
            reply = self.chatGPT.getReply()
            self.memorize(prompt, reply, "")
            
            return reply
        except Exception as e:
            return str(e)
    
    def askWithImage(self, imagePath: str, prompt: str) -> str:
        """
        Method to post request with image to chatgpt
        
        :param imagePath: where the image is
        :param prompt: what user asked to chatgpt
        
        :return: chatgpt's reply
        
        :raise e: all exceptions happenned during processing
        """
        try:
            imageEditer = ImageEditer()
            image = imageEditer.open(imagePath)
            
            # width > height
            if image.size[0] > image.size[1]:
                image = imageEditer.resizeByWidth(image, 512)
            else:
                image = imageEditer.resizeByHeight(image, 512)
            imageEditer.save(image, 'forVision.jpg')
            encordedImage = self.chatGPT.setPicture(url='forVision.jpg', pronpt=prompt)
            reply = self.chatGPT.getReply()
            imageEditer.remove('forVision.jpg')
            self.memorize(prompt, reply, encordedImage)
            
            return reply
        except Exception as e:
            return str(e)
        