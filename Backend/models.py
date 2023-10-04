
from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base

class ChatLog(Base):
    __tablename__ = "chat_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_prompt = Column(String, index=True)
    bot_response = Column(String)
    timestamp = Column(DateTime(timezone=True), default=func.now())
