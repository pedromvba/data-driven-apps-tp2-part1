from pydantic import BaseModel

class TranslatorModel(BaseModel):
    message: str

class ChatReponseModel(BaseModel):
    bot_message: str