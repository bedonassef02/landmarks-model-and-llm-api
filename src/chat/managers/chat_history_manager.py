from src.chat.utils.chat_history import ChatHistory, Session


class ChatHistoryManager:
    def __init__(self):
        self.chatHistory = ChatHistory

    def get_chat_history(self, ip_address):
        session = Session()
        chat_history = (
            session.query(ChatHistory)
            .filter_by(ip_address=ip_address)
            .order_by(ChatHistory.id.desc())  # Order by ID in descending order to get the latest messages first
            .limit(3)  # Limit the number of results to 3
            .all()
        )
        session.close()
        return [(conv.user_question, conv.bot_answer) for conv in
                reversed(chat_history)]  # Reverse the list to get messages in chronological order

    def store_chat_history(self, ip_address, user_question, bot_answer):
        session = Session()
        new_conversation = ChatHistory(ip_address=ip_address, user_question=user_question, bot_answer=bot_answer)
        session.add(new_conversation)
        session.commit()
        session.close()
