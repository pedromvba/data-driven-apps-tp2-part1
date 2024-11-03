#import json
from fastapi import APIRouter
from transformers import pipeline
from models.textTranslatorModel import TranslatorModel, ChatReponseModel
import torch

router = APIRouter()

# if device is uncommented, it goes on the pipeline method as an argument
#device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

def generate_text(message:str) -> dict:
    generator = pipeline(model='Helsinki-NLP/opus-mt-en-fr')
    text = generator(message)
    return text

@router.post('/en-fr-translator/')
async def translator(body: TranslatorModel) -> ChatReponseModel:
    response = generate_text(body.message)
    return ChatReponseModel(bot_message=response[0]['translation_text'])