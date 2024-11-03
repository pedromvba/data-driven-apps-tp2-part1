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

# def generate_text(message:dict) -> dict:
#     generator = pipeline('text-generation', model='gpt2')
#     text = generator(message['text'])
#     return text

@router.post('/textgen/')
async def autocomplete(body:TextGeneratorModel) -> ChatReponseModel:
    response = generate_text(body.message)
    return ChatReponseModel(bot_message=response[0]['generated_text'])
    



















# @router.get('/user/{username}', response_model=TextGeneratorModel)
# def greetings(username:str):
#     with open('data/users.json') as file: # read data from json file
#         data = json.load(file)
#         usernames = [user['name'].lower() for user in data]

#     if username.lower() not in usernames: # check if user exists
#         raise HTTPException(status_code=404, detail='User not found')
    
#     return {'username':username.capitalize(),
#             'message':f'Hello {username.capitalize()}'
