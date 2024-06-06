import numpy as np
from keras.preprocessing import image
from src.model.helpers.data_augmentation import train_generator
from src.model.helpers.load_models import models

class ImageClassPredictor:
    NUMBER_OF_CLASSES = 53

    def __init__(self, train_generator, models):
        """
        Initialize the ImageClassPredictor.

        :param train_generator: The training data generator.
        :param models: List of models for ensemble prediction.
        """
        self.train_generator = train_generator
        self.models = models

    @staticmethod
    def preprocess_image(img):
        """
        Preprocess the input image for prediction.

        :param img: Input image.
        :return: Preprocessed image array.
        """
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.
        return img_array

    def predict_image_class(self, img):
        """
        Predict the class label for the input image.

        :param img: Input image.
        :return: Predicted class label.
        """
        img_array = self.preprocess_image(img)

        predictions = np.zeros((1, self.NUMBER_OF_CLASSES))
        for model in self.models:
            model_predictions = model.predict(img_array)
            predictions += model_predictions

        ensemble_predictions = predictions / len(self.models)

        # Get top 5 predictions
        top_5_indices = np.argsort(ensemble_predictions[0])[-5:][::-1]
        top_5_accuracies = ensemble_predictions[0][top_5_indices]

        predicted_class_labels = self.train_generator.class_indices
        predicted_class_labels = {v: k for k, v in predicted_class_labels.items()}

        top_5_labels = [predicted_class_labels[idx] for idx in top_5_indices]

        top_5_predictions = list(zip(top_5_labels, top_5_accuracies))

        for label, accuracy in top_5_predictions:
            print(f"Class: {label}, Accuracy: {accuracy:.4f}")

        if top_5_accuracies[0] < 0.5:  # If maximum predicted probability is less than 50%
            return "unknown"

        return top_5_labels[0]  # Return the top prediction
