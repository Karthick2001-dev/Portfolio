from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from LLM import get_llm_response

app = FastAPI()

# ✅ FIX: Allow frontend (http://127.0.0.1:5500) to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can change ["*"] to ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, OPTIONS, etc.
    allow_headers=["*"],  # Allows all headers
)

class QuestionRequest(BaseModel):
    question: str

@app.post("/chat")
async def chat(request: QuestionRequest):
    response = get_llm_response(request.question)
    return {"response": response}
