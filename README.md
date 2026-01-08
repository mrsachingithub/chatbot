# AI Chatbot Project

This project implements a chatbot using a modern web architecture:
- **Frontend**: React (Vite)
- **Backend**: FastAPI (Python)
- **Logic**: Custom NLP Engine (Placeholder)

## Dictionary

- `backend/`: Contains the FastAPI application and NLP logic.
- `frontend/`: Contains the React web application.

## Prerequisites

- Python 3.8+
- Node.js & npm

## Setup & Running

### 1. Backend

The backend runs on `http://localhost:8000`.

```bash
cd backend
# Create virtual environment (optional but recommended)
python -m venv venv
# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload --port 8000
```

### 2. Frontend

The frontend runs on `http://localhost:5173`.

```bash
cd frontend
# Install dependencies
npm install

# Start the development server
npm run dev
```

## Features

- **Basic Chat**: Responds to greetings.
- **Arithmetic**: Solves basic math problems (e.g., `10 + 20`, `50 / 2`).
- **Knowledge Base**: Answers questions from `Conversation.csv` and `conversation.txt`.

## detailed Usage

1. Open your browser to the URL shown by the frontend (usually `http://localhost:5173`).
2. Type a message (e.g., "Hello", "Time", "What is the capital of Egypt?") into the input box.
3. The chatbot will respond based on the logic defined in `backend/nlp_engine.py`.

## Configuration

The backend uses a `.env` file for configuration.
- `CSV_FILENAME`: Name of the CSV file in the directory.
- `TXT_FILENAME`: Name of the TXT file in the directory.