import tensorflow as tf

model_paths = [
    # "densenet_169_-saved-model-93-acc-0.90.keras",
    # "densenet_201_-saved-model-91-acc-0.90.keras",
    # "inception_resnset_v2_-saved-model-88-acc-0.90.keras",
    # "vgg_16_-saved-model-70-acc-0.89.keras",
    # "xception_-saved-model-07-acc-0.93.keras",
    "xception_-saved-model-77-acc-0.91.keras",
    # "densenet_121_-saved-model-94-acc-0.89.keras",
    # "inception_resnet_-saved-model-97-acc-0.88.keras",
    # "resnet_101_-saved-model-88-acc-0.88.keras",
    # "densenet_201_-saved-model-97-acc-0.87.keras",
    # "mobilenet_50_-saved-model-87-acc-0.85.keras",
]

models = []
for path in model_paths:
    try:
        model = tf.keras.models.load_model('keras/' + path, compile=False)
        models.append(model)
    except Exception as e:
        print(f"Error loading model {path}: {e}")
