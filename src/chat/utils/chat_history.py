from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Initialize SQLAlchemy engine
engine = create_engine('sqlite:///chat_history.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Define a model for chat history
class ChatHistory(Base):
    __tablename__ = 'chat_history'
    id = Column(Integer, primary_key=True)
    ip_address = Column(String(100))
    user_question = Column(Text)
    bot_answer = Column(Text)

# Create the table if it doesn't exist
Base.metadata.create_all(engine)