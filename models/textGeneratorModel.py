from pydantic import BaseModel

class TextGeneratorModel(BaseModel):
    message: str

# class TextGeneratorModel(BaseModel):
#     message: dict

class ChatReponseModel(BaseModel):
    bot_message: str