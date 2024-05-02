import json
from src.chat.utils.chat_assistant import ChatAssistant
from src.chat.managers.chat_history_manager import ChatHistoryManager

chatHistoryManager = ChatHistoryManager()

monuments_and_landmarks = []

with open('monuments_and_landmarks.json', 'r', encoding='utf-8') as file:
    monuments_and_landmarks = json.load(file)

monuments_and_landmarks = monuments_and_landmarks[::-1]

for class_name in monuments_and_landmarks:
    print(class_name)
    chatAssistant = ChatAssistant(class_name)
    question = "give me info about " + class_name
    ans = chatAssistant.process_user_input(question, "127.0.0.1")
    chatHistoryManager.store_chat_history(user_question=question, bot_answer=ans, ip_address="127.0.0.1")
