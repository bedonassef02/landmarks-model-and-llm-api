from flask import Blueprint, request, jsonify
from src.model.data_augmentation import IMG_SIZE
from keras.preprocessing import image
from src.model.predict import predict_image_class
from io import BytesIO

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
        predicted_class = predict_image_class(img)
        return jsonify({'predicted_class': predicted_class})

    return jsonify({'error': 'Unknown error occurred'}), 500
