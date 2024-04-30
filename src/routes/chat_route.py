from flask import Blueprint, request, jsonify
from src.chat.utils.random_question_generator import RandomQuestionGenerator
from src.chat.managers.chat_history_manager import ChatHistoryManager
from src.chat.utils.chat_assistant import ChatAssistant
from src.utils.class_name_exist import is_class_exist

chat_route = Blueprint('chat', __name__)

chatHistoryManager = ChatHistoryManager()
randomQuestionGenerator = RandomQuestionGenerator()

@chat_route.route('/chat', methods=['POST'])
def chat():
    data = request.json
    print(data)
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    user_question = data.get('user_question')
    class_name = data.get('class_name')

    if not user_question and not class_name:
        return jsonify({'error': 'No user question or class name provided'}), 400

    user_ip = request.remote_addr

    chat_assistant = ChatAssistant(class_name) if class_name and is_class_exist(class_name) else ChatAssistant()

    if class_name and is_class_exist(class_name):
        user_question = user_question or f'give me info about {class_name}'
        # answer = user_input(class_name, user_question, user_ip)
        answer = chat_assistant.process_user_input(user_question, user_ip)
    else:
        # answer = ans_question(user_question, user_ip)
        answer = chat_assistant.answer_question(user_question, user_ip)

    chatHistoryManager.store_chat_history(user_ip, user_question, answer)

    return jsonify(answer)


@chat_route.route('/suggest', methods=['GET'])
def suggest():
    questions = randomQuestionGenerator.generate_random_questions();

    return jsonify(questions)
