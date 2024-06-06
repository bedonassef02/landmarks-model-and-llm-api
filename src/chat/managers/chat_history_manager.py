import logging
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from src.chat.utils.chat_history import ChatHistory, Session

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error(f"Session rollback due to error: {e}")
        raise
    finally:
        session.close()

class ChatHistoryManager:
    def __init__(self):
        """
        Initialize the ChatHistoryManager.
        """
        self.chat_history_model = ChatHistory

    def get_chat_history(self, ip_address, limit=3):
        """
        Retrieve the chat history for a given IP address.

        :param ip_address: The IP address to filter chat history by.
        :param limit: The number of chat history entries to retrieve.
        :return: A list of tuples containing user questions and bot answers.
        """
        with session_scope() as session:
            chat_history = (
                session.query(self.chat_history_model)
                .filter_by(ip_address=ip_address)
                .order_by(self.chat_history_model.id.desc())  # Order by ID in descending order to get the latest messages first
                .limit(limit)
                .all()
            )
            logger.info(f"Retrieved {len(chat_history)} chat history entries for IP: {ip_address}")
            return [(conv.user_question, conv.bot_answer) for conv in reversed(chat_history)]  # Reverse the list to get messages in chronological order

    def store_chat_history(self, ip_address, user_question, bot_answer):
        """
        Store a new chat history entry.

        :param ip_address: The IP address of the user.
        :param user_question: The user's question.
        :param bot_answer: The bot's answer.
        """
        new_conversation = self.chat_history_model(ip_address=ip_address, user_question=user_question, bot_answer=bot_answer)
        with session_scope() as session:
            session.add(new_conversation)
            logger.info(f"Stored new chat history entry for IP: {ip_address}")
