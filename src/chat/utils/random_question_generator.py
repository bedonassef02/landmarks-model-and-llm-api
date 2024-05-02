import json
import random


class RandomQuestionGenerator:
    def __init__(self, file_path='suggestion.json'):
        self.file_path = file_path

    def load_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def select_random_classes(self, data, num_classes=3):
        return random.sample(data, num_classes)

    def generate_random_questions(self, num_classes=3):
        data = self.load_data()
        random_classes = self.select_random_classes(data, num_classes)

        questions = []
        for item in random_classes:
            selected_question = random.choice(item['questions'])
            questions.append({"className": item['name'], "question": selected_question, "emojis": item["emojis"]})

        return questions
