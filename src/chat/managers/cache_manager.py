class CacheManager:
    def __init__(self):
        self.cache = {}

    def get_from_cache(self, class_name, user_question):
        key = (class_name, user_question)
        if key in self.cache:
            print("Cache hit!")
            return self.cache[key]
        else:
            print("Cache miss!")
            return None

    def add_to_cache(self, class_name, user_question, answer):
        key = (class_name, user_question)
        self.cache[key] = answer
        print("Added to cache.")
