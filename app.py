import os
import spacy
import requests
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Load spaCy model for NER
nlp = spacy.load("en_core_web_sm")

# Hugging Face Inference API URL and Token
HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
HF_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

app = FastAPI()

# Serve static files from "/static" path
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the HTML page at "/"
@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html") as f:
        return f.read()

# Process prompt endpoint
@app.post("/process_prompt")
async def process_prompt(prompt: str = Form(...)):
    # NER
    doc = nlp(prompt)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # LLM
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {"inputs": prompt}

    response = requests.post(HF_API_URL, headers=headers, json=payload)
    response_data = response.json()

    try:
        llm_output = response_data[0]['generated_text']
    except Exception as e:
        llm_output = str(response_data)

    return JSONResponse(content={
        "entities": entities,
        "llm_response": llm_output
    })
