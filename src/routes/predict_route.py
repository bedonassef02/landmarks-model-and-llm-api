from flask import Blueprint, request, jsonify
from src.model.helpers.data_augmentation import IMG_SIZE
from keras.preprocessing import image
from src.model.image_class_predictor import ImageClassPredictor
from io import BytesIO
from src.utils.class_name_exist import monuments_and_landmarks
import os
import uuid

imageClassPredictor = ImageClassPredictor()

predict_route = Blueprint('predict', __name__)


@predict_route.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        print("No File Part")
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        print("No selected file")
        return jsonify({'error': 'No selected file'}), 400
    if file:
        file_stream = BytesIO(file.read())
        img = image.load_img(file_stream, target_size=IMG_SIZE)
        predicted_class = imageClassPredictor.predict_image_class(img)

        # Save the image with the class name as its filename
        unique_id = str(uuid.uuid4())

        save_dir = os.path.join("uploads", predicted_class)
        os.makedirs(save_dir, exist_ok=True)

        save_path = os.path.join(save_dir, f"{predicted_class}_{unique_id}.jpg")
        image.save_img(save_path, image.load_img(file_stream))

        return jsonify(predicted_class)

    print("Unknown error occurred'")
    return jsonify({'error': 'Unknown error occurred'}), 500


@predict_route.route('/classes', methods=['GET'])
def monuments_landmarks():
    return jsonify(monuments_and_landmarks), 200
