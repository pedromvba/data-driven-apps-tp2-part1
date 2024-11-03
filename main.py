# imports
from fastapi import FastAPI
from routes.textGenerator import router as text_generator_router
from routes.textTranslator import router as text_translator_router
#from routers.status import router as status_router


# FastAPI instance
app = FastAPI()

# calling endpoints and methods
app.include_router(text_generator_router)
# app.include_router(user_router)


# root route
@app.get('/')
def root():
    return {'message':'Hello - Services avaiables: text generator @/textgen/ and text translator @/translator/'}