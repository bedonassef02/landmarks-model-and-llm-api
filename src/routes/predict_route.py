from flask import Blueprint, request, jsonify
from keras.preprocessing import image
from io import BytesIO
import os
import uuid

from src.model.helpers.data_augmentation import IMG_SIZE, train_generator
from src.model.helpers.load_models import models
from src.model.image_class_predictor import ImageClassPredictor
from src.utils.class_name_exist import monuments_and_landmarks

imageClassPredictor = ImageClassPredictor(train_generator, models)

predict_route = Blueprint('predict', __name__)


@predict_route.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
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
        img.save(save_path)

        return jsonify(predicted_class), 200

    return jsonify({'error': 'Unknown error occurred'}), 500


@predict_route.route('/classes', methods=['GET'])
def monuments_landmarks():
    return jsonify(monuments_and_landmarks), 200
