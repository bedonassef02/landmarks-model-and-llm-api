import json

monuments_and_landmarks = []

with open('monuments_and_landmarks.json', 'r', encoding='utf-8') as file:
    monuments_and_landmarks = json.load(file)


def is_class_exist(class_name):
    return class_name in monuments_and_landmarks
