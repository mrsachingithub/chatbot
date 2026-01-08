from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from nlp_engine import process_query

# --- Configuration ---
app = FastAPI(
    title="Simple AI Chatbot",
    description="A FastAPI backend for the chatbot application.",
    version="1.0.0"
)

# --- Middleware ---
# Allow all origins for development. In production, restrict this.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Data Models ---
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

# --- Endpoints ---

@app.get("/")
async def root():
    """
    Health check endpoint to verify backend is running.
    """
    return {"message": "Chatbot API is operational"}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Process a user message and return the chatbot's response.
    """
    if not request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    response_text = process_query(request.message)
    return ChatResponse(response=response_text)
