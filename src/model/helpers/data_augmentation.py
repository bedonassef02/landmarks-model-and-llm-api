from tensorflow.keras.preprocessing.image import ImageDataGenerator

EXTRACTED_FOLDER = "images"
IMG_SIZE = (150, 150)

datagen = ImageDataGenerator()

train_generator = datagen.flow_from_directory(
    EXTRACTED_FOLDER,
    target_size=IMG_SIZE,
)