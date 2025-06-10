# app.py

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import spacy
import requests

app = FastAPI()

# Serve static files at /static
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# Serve index.html at root /
@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse("static/index.html")

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Ollama API URL
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3"  # Change to the model you are running

# POST endpoint to process prompt
@app.post("/process_prompt")
async def process_prompt(prompt: str = Form(...)):
    # --- NER ---
    doc = nlp(prompt)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # --- LLM ---
    ollama_payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    ollama_response = requests.post(OLLAMA_URL, json=ollama_payload)
    llm_output = ollama_response.json().get("response", "")

    # --- Logging ---
    print("Prompt received:", prompt)
    print("Named Entities:", entities)
    print("LLM Response:", llm_output)

    # Return JSON response
    return JSONResponse(content={
        "entities": entities,
        "llm_response": llm_output
    })
