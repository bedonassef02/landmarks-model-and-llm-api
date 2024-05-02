from flask import Blueprint, request, jsonify
from src.chat.utils.random_question_generator import RandomQuestionGenerator
from src.chat.managers.chat_history_manager import ChatHistoryManager
from src.utils.process_chat_request import process_chat_request
from src.utils.generate_suggestions import generate_suggestions

chat_route = Blueprint('chat', __name__)

chatHistoryManager = ChatHistoryManager()
randomQuestionGenerator = RandomQuestionGenerator()


@chat_route.route('/chat', methods=['POST'])
def chat():
    data = request.json
    print(data)
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    user_ip = request.remote_addr
    return process_chat_request(data, user_ip)


@chat_route.route('/suggest', methods=['GET'])
def suggest():
    return generate_suggestions()
