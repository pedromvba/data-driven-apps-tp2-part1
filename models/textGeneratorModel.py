from pydantic import BaseModel

class TextGeneratorModel(BaseModel):
    input_text: str

# class TextGeneratorModel(BaseModel):
#     input_text: dict

class ChatReponseModel(BaseModel):
    bot_message: str