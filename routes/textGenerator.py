#import json
from fastapi import APIRouter
from transformers import pipeline
from models.textGeneratorModel import TextGeneratorModel, ChatReponseModel
import torch

router = APIRouter()

def generate_text(message:str) -> dict:
    generator = pipeline('text-generation', model='gpt2', max_length=30, num_return_sequences=1)
    text = generator(message)
    return text

@router.post('/textgen/')
async def autocomplete(body:TextGeneratorModel) -> ChatReponseModel:
    response = generate_text(body.message)
    return ChatReponseModel(bot_message=response[0]['generated_text'])
