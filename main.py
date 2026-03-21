from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from mistralai import Mistral
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()

app = FastAPI()

# Serve frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Connect to Mistral
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

# This defines what a chat message looks like
class Message(BaseModel):
    message: str

# This is the chat endpoint - frontend sends message here
@app.post("/chat")
async def chat(data: Message):
    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[{"role": "user", "content": data.message}]
    )
    return JSONResponse({"reply": response.choices[0].message.content})

# Homepage
@app.get("/")
async def root():
    return JSONResponse({"message": "Chatbot is running!"})