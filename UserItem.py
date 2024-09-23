from pydantic import BaseModel
from typing_extensions import Union
from typing import List

##class to store conversation of user
class Conversation(BaseModel):
    conversationId: int
    text:str

## class to store the user details
class UserItemAll(BaseModel):
    name:str
    id:str
    conversationList:Union[List[Conversation],None]=None
     
    # # Add conversation method with auto-increment
    # def add_conversation(self, text: str):
    #     new_conversation_id = (self.conversationList[-1].conversationId + 1 
    #                            if self.conversationList else 1)
    #     new_conversation = Conversation(conversationId=new_conversation_id, text=text)
    #     self.conversationList.append(new_conversation)

class User(UserItemAll):
    pass


