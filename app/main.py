from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Mock LLM Demo")

# ✅ Allow frontend (React) to access FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
async def root():
    return {"message": "Mock LLM demo running successfully!"}

@app.post("/ask")
async def ask_ai(request: PromptRequest):
    user_input = request.prompt.lower()

    if "reinforcement learning" in user_input:
        return JSONResponse(content={
            "response": "Reinforcement learning is an area of machine learning where agents learn by interacting with an environment and receiving rewards or penalties."
        })
    
    elif "neural network" in user_input:
        return JSONResponse(content={
            "response": "A neural network is a set of algorithms that model complex relationships between inputs and outputs."
        })
    
    else:
        return JSONResponse(content={
            "response": "I'm not sure about that yet, could you rephrase?"
        })
