import logging
from src.chat.managers.chat_history_manager import ChatHistoryManager
from src.chat.managers.conversational_chain_manager import ConversationalChainManager

logger = logging.getLogger(__name__)

class QuestionAnswerer:
    def __init__(self, chain_manager=None, history_manager=None):
        """
        Initialize the QuestionAnswerer.

        :param chain_manager: Instance of ConversationalChainManager.
        :param history_manager: Instance of ChatHistoryManager.
        """
        self.conversational_chain_manager = chain_manager or ConversationalChainManager()
        self.chat_history_manager = history_manager or ChatHistoryManager()

    def generate_answer(self, user_question, user_ip, vector_store):
        """
        Generate an answer for the given user question.

        :param user_question: The user's question.
        :param user_ip: The user's IP address.
        :param vector_store: Vector store for similarity search.
        :return: The generated answer.
        """
        try:
            docs = vector_store.similarity_search(user_question)
            chain = self.conversational_chain_manager.get_conversational_chain()
            previous_conversations = self.chat_history_manager.get_chat_history(user_ip)

            response = chain.invoke(
                {"input_documents": docs, "question": user_question, "previous_conversations": previous_conversations},
                return_only_outputs=True)

            answer = response['output_text']
            return answer

        except Exception as e:
            logger.error("Error generating answer: %s", str(e))
            return "Sorry, I couldn't generate an answer at the moment."
