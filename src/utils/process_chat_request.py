from flask import jsonify
from src.chat.utils.chat_assistant import ChatAssistant
from src.utils.class_name_exist import is_class_exist
from src.chat.managers.chat_history_manager import ChatHistoryManager

chatHistoryManager = ChatHistoryManager()


def process_chat_request(data, user_ip):
    user_question = data.get('user_question')
    class_name = data.get('class_name')

    if not user_question and not class_name:
        return jsonify({'error': 'No user question or class name provided'}), 400

    chat_assistant = ChatAssistant(class_name) if class_name and is_class_exist(class_name) else ChatAssistant()

    if class_name and is_class_exist(class_name):
        user_question = user_question or f'give me info about {class_name}'
        answer = chat_assistant.process_user_input(user_question, user_ip)
    else:
        answer = chat_assistant.answer_question(user_question, user_ip)

    chatHistoryManager.store_chat_history(user_ip, user_question, answer)

    return jsonify(answer)
