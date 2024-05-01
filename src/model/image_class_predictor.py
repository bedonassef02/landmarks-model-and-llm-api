import numpy as np
from keras.preprocessing import image
from src.model.helpers.data_augmentation import train_generator
from src.model.helpers.load_models import models

class ImageClassPredictor:
    NUMBER_OF_CLASSES = 53

    def __init__(self):
        self.train_generator = train_generator
        self.models = models

    def img_to_array(self, img):
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.
        return img_array

    def predict_image_class(self, img):
        img_array = self.img_to_array(img)

        predictions = np.zeros((1, self.NUMBER_OF_CLASSES))
        for model in self.models:
            model_predictions = model.predict(img_array)
            predictions += model_predictions

        ensemble_predictions = predictions / len(self.models)
        max_prediction = np.max(ensemble_predictions)

        if max_prediction < 0.5: # If maximum predicted probability is less than 50%
            return "unknown"

        predicted_class_index = np.argmax(ensemble_predictions)
        predicted_class_label = self.train_generator.class_indices
        predicted_class_label = dict((v, k) for k, v in predicted_class_label.items())
        predicted_class_label = predicted_class_label[predicted_class_index]

        return predicted_class_label
