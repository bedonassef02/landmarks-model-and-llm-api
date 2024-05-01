import json
from src.chat.utils.question_answerer import QuestionAnswerer
from src.chat.managers.chat_history_manager import ChatHistoryManager

chatHistoryManager = ChatHistoryManager()

monuments_and_landmarks = []

with open('monuments_and_landmarks.json', 'r', encoding='utf-8') as file:
    monuments_and_landmarks = json.load(file)

for class_name in monuments_and_landmarks:
    print(class_name)
    question = "give me info about " + class_name
    ans = user_input(class_name, question, "127.0.0.1")
    chatHistoryManager.store_chat_history(user_question=question, bot_answer=ans, ip_address="127.0.0.1")
