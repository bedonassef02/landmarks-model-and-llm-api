from src.chat.managers.cache_manager import CacheManager
from src.chat.utils.question_answerer import QuestionAnswerer
from src.chat.managers.vector_store_manager import VectorStoreManager

class ChatAssistant:
    def __init__(self, class_name=None):
        self.class_name = class_name
        self.question_answerer = QuestionAnswerer()
        self.vector_store_manager = VectorStoreManager()
        self.cacheManager = CacheManager()
        self.all_classes_vector_store = None

    def _get_vector_store(self):
        if self.class_name:
            return self.vector_store_manager.get_vectorstore_fofinr_class(self.class_name)
        else:
            if not self.all_classes_vector_store:
                self.all_classes_vector_store = self.vector_store_manager.get_vectorstore_for_all()
            return self.all_classes_vector_store

    def process_user_input(self, user_question, user_ip):
        cached_response = self.cacheManager.get_from_cache(self.class_name, user_question)
        if cached_response:
            return cached_response

        vector_store = self._get_vector_store()
        answer = self.question_answerer.generate_answer(user_question, user_ip, vector_store)

        self.cacheManager.add_to_cache(self.class_name, user_question, answer)
        return answer

    def answer_question(self, user_question, user_ip):
        cached_response = self.cacheManager.get_from_cache("", user_question)
        if cached_response:
            return cached_response

        vector_store = self._get_vector_store()
        answer = self.question_answerer.generate_answer(user_question, user_ip, vector_store)

        self.cacheManager.add_to_cache("", user_question, answer)
        return answer
