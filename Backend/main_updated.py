from fastapi import FastAPI, HTTPException, Depends
from schemas import ChatRequest, ChatResponse
from services_updated import create_conversation, delete_conversation, generate_response, update_conversation
from datetime import datetime
from sqlalchemy.orm import Session
from database_updated import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate/", response_model=ChatResponse)
def generate_text(request: ChatRequest, db: Session = Depends(get_db)):
    try:
        # Generate a response from the Llama-2 model
        response_text = generate_response(request.prompt)
        chat_log = create_conversation(db, request.prompt, response_text)
        return {"response": response_text, "timestamp": chat_log.timestamp}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/update_conversation/{chat_id}/")
def update_chat(chat_id: int, user_prompt: str = None, bot_response: str = None, db: Session = Depends(get_db)):
    updated_chat = update_conversation(db, chat_id, user_prompt, bot_response)
    if not updated_chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return updated_chat

@app.delete("/delete_conversation/{chat_id}/")
def delete_chat(chat_id: int, db: Session = Depends(get_db)):
    deleted_chat = delete_conversation(db, chat_id)
    if not deleted_chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return {"status": "success", "message": f"Deleted chat with ID {chat_id}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
