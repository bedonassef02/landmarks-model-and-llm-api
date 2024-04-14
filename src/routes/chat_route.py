from flask import Blueprint, request, jsonify
from src.llm import user_input

chat_route = Blueprint('chat', __name__)


@chat_route.route('/chat', methods=['POST'])
def chat():
    data = request.json
    if not data or 'class_name' not in data:
        return jsonify({'error': 'No class_name provided'}), 400

    class_name = data['class_name']
    user_question = data.get('user_question',
                             'give me info about ' + class_name)

    response = user_input(class_name, user_question)

    return jsonify({'response': response})
