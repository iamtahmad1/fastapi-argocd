# main.py

from fastapi import FastAPI
from customproject_helloworld import api

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World production"}

    
@app.get("/customproject_helloworld")
def customproject_helloworld():
    return api.customproject_helloworld()