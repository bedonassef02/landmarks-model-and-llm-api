cache = {}


def get_from_cache(class_name, user_question):
    key = (class_name, user_question)
    if key in cache:
        print("Cache hit!")
        return cache[key]
    else:
        print("Cache miss!")
        return None


def add_to_cache(class_name, user_question, answer):
    key = (class_name, user_question)
    cache[key] = answer
    print("Added to cache.")
