import logging
from src.chat.managers.cache_manager import CacheManager
from src.chat.utils.question_answerer import QuestionAnswerer
from src.chat.managers.vector_store_manager import VectorStoreManager

logger = logging.getLogger(__name__)

class ChatAssistant:
    def __init__(self, class_name=None, cache_manager=None, question_answerer=None, vector_store_manager=None):
        self.class_name = class_name
        self.cache_manager = cache_manager or CacheManager()
        self.question_answerer = question_answerer or QuestionAnswerer()
        self.vector_store_manager = vector_store_manager or VectorStoreManager()
        self.all_classes_vector_store = None

    def _get_vector_store(self):
        if self.class_name:
            return self.vector_store_manager.get_vectorstore_for_class(self.class_name)
        else:
            if not self.all_classes_vector_store:
                self.all_classes_vector_store = self.vector_store_manager.get_vectorstore_for_all()
            return self.all_classes_vector_store

    def process_user_input(self, user_question, user_ip):
        try:
            cached_response = self.cache_manager.get_from_cache(self.class_name, user_question)
            if cached_response:
                logger.info("Cache hit for user_question: %s", user_question)
                return cached_response

            vector_store = self._get_vector_store()
            answer = self.question_answerer.generate_answer(user_question, user_ip, vector_store)

            self.cache_manager.add_to_cache(self.class_name, user_question, answer)
            return answer
        except Exception as e:
            logger.error("An error occurred while processing user input: %s", str(e))
            return "An error occurred while processing your request."

    def answer_question(self, user_question, user_ip):
        try:
            cached_response = self.cache_manager.get_from_cache("", user_question)
            if cached_response:
                logger.info("Cache hit for user_question: %s", user_question)
                return cached_response

            vector_store = self._get_vector_store()
            answer = self.question_answerer.generate_answer(user_question, user_ip, vector_store)

            self.cache_manager.add_to_cache("", user_question, answer)
            return answer
        except Exception as e:
            logger.error("An error occurred while answering question: %s", str(e))
            return "An error occurred while processing your request."
