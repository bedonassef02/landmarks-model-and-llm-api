from flask import jsonify
from src.chat.utils.random_question_generator import RandomQuestionGenerator

randomQuestionGenerator = RandomQuestionGenerator()


def generate_suggestions():
    questions = randomQuestionGenerator.generate_random_questions()
    return jsonify(questions)
