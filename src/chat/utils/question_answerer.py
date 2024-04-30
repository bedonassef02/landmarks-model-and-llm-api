from src.chat.managers.chat_history_manager import ChatHistoryManager
from src.chat.managers.conversational_chain_manager import ConversationalChainManager

chatHistoryManager = ChatHistoryManager()

class QuestionAnswerer:
    def __init__(self):
        self.conversationalChainManager = ConversationalChainManager()
        self.chatHistoryManager = ChatHistoryManager()

    def generate_answer(self, user_question, user_ip, vector_store):
        docs = vector_store.similarity_search(user_question)

        chain = self.conversationalChainManager.get_conversational_chain()

        previous_conversations = self.chatHistoryManager.get_chat_history(user_ip)

        response = chain(
            {"input_documents": docs, "question": user_question, "previous_conversations": previous_conversations},
            return_only_outputs=True)

        answer = response['output_text']

        return answer
