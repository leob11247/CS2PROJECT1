import openai
import base64

class ChatGPT:
    def __init__(self) -> None:
        """
        Method to initialize chatgpt
        """
        self.model = 'gpt-4-turbo'
        self.messages = []
        self.isBlocked = False
        self.apiKey = None
        
    def setAPIKey(self, apiKey: str) -> None:
        """
        Method to set API key.
        :param apiKey: API key
        """
        self.apiKey = apiKey
        openai.api_key = apiKey
        
    def clearConversation(self) -> None:
        """
        Method to reset chat history.
        """
        self.messages = []
        
    def setModel(self, model: str) -> None:
        """
        Method to select chatgpt model.
        :param model: chatgpt model name
        """
        self.model = model
    
    def setSystemRole(self, content: str) -> None:
        """
        Method to set system role of chatgpt
        :param content: prompt of system role
        """
        self.setMessage(role="system", content=content)
        
    def setMessage(self, role: str, content: str) -> None:
        """
        Method to set message to chat history
        :param role: whose statement. (user, assistant or systemRole)
        :param content: prompt to record
        """
        self.messages.append({"role": role, "content": content})
        
    def setPicture(self, url: str, pronpt: str) -> str:
        """
        Method to set picture to chat history
        :param: url: where image is located
        :param prompt: prompt to record with the picture
        
        :return: value of photo changed to base64 format
        
        :raise e: all exception happenned during processing
        """
        try:
            with open(url, "rb") as image_file:
                encodedImage = base64.b64encode(image_file.read()).decode("utf-8")
                self.messages.append({
                    "role": "user",
                    "content": [
                        {"type": "text", "text": pronpt}, 
                        {"type": "image_url","image_url": {"url": f"data:image/jpeg;base64,{encodedImage}"}}, 
                    ],
                })
            return encodedImage
        except Exception as e:
            raise e
    
    def setEncordedPicture(self, encordedImage: str, prompt: str) -> None:
        """
        Method to set picture to chat history
        :param encordedImage: image encorded base64 format
        :param prompt: prompt to record with the picture
        
        :raise e: all exception happenned during processing
        """
        self.messages.append({
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt}, 
                    {"type": "image_url","image_url": {"url": f"data:image/jpeg;base64,{encordedImage}"}}, 
                ],
            })
    
    def getReply(self) -> str:
        if self.isBlocked:
            return "api request is blocked now."
        else:
            try:
                chat = openai.ChatCompletion.create(model=self.model, messages=self.messages, max_tokens=1000)
                self.setMessage('assistant', chat.choices[0].message.content)
                return chat.choices[0].message.content
            except Exception as e:
                raise e
