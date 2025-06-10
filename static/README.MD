# 🦙 LLM + NER Demo (Founding Team Coding Challenge)

This is a demo application for the coding challenge — combines:

✅ FastAPI Backend  
✅ spaCy Named Entity Recognition (NER)  
✅ Local LLM via Ollama (tested with LLaMA 3)  
✅ Simple HTML Frontend  
✅ Deployable with Docker / HuggingFace Spaces  

---

## How it works

1️⃣ User enters a **prompt** in the web UI → clicks "Send"  
2️⃣ Backend:
- extracts **Named Entities** using `spaCy en_core_web_sm`
- queries **Local LLM** via `Ollama REST API` running locally
3️⃣ Displays:
- Detected entities
- LLM response

---

## Example prompt

> "Barack Obama was born in Hawaii and became the President of the United States."

→ Entities:
- Barack Obama → PERSON  
- Hawaii → GPE  
- United States → GPE  

→ LLM response: _(Example sentence from LLaMA3)_

---

## Deployment

### Run locally:

```bash
uvicorn app:app --reload
