
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the model and tokenizer
MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

def generate_response(prompt: str) -> str:
    # Tokenize the input prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate a response from the model
    output = model.generate(input_ids, max_length=200, num_return_sequences=1, top_k=10)
    
    # Decode the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text




# CRUD functions for ChatLog

def create_conversation(db: Session, user_prompt: str, bot_response: str):
    """Insert a new conversation into the database."""
    chat_log = ChatLog(user_prompt=user_prompt, bot_response=bot_response)
    db.add(chat_log)
    db.commit()
    db.refresh(chat_log)
    return chat_log

def update_conversation(db: Session, chat_id: int, user_prompt: str = None, bot_response: str = None):
    """Modify an existing conversation."""
    chat_log = db.query(ChatLog).filter(ChatLog.id == chat_id).first()
    if chat_log:
        if user_prompt:
            chat_log.user_prompt = user_prompt
        if bot_response:
            chat_log.bot_response = bot_response
        db.commit()
        db.refresh(chat_log)
        return chat_log
    return None

def delete_conversation(db: Session, chat_id: int):
    """Delete a conversation based on its id."""
    chat_log = db.query(ChatLog).filter(ChatLog.id == chat_id).first()
    if chat_log:
        db.delete(chat_log)
        db.commit()
    return chat_log
