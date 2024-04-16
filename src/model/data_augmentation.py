from keras.src.legacy.preprocessing.image import ImageDataGenerator

EXTRACTED_FOLDER = r"D:\BEDO\UNIVERSITY\FCAI-HU\GP\dataset\Custom\06.2"
IMG_SIZE = (150, 150)

datagen = ImageDataGenerator()

train_generator = datagen.flow_from_directory(
    EXTRACTED_FOLDER,
    target_size=IMG_SIZE,
)
