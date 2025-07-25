from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI(title="Text Generation API", description="A simple API for generating text using Groq")

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is required")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile"

class TextRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Text Generation API is running!", "status": "healthy"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/generate-text")
def generate_text(req: TextRequest):
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": req.prompt
            }
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.post(GROQ_URL, json=payload, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to generate text")
    data = response.json()
    try:
        return {"response": data["choices"][0]["message"]["content"]}
    except (KeyError, IndexError):
        raise HTTPException(status_code=500, detail="Invalid response from model")