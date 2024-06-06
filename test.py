import tensorflow as tf

model = tf.keras.models.load_model('keras/vgg_16_-saved-model-70-acc-0.89.keras')

print(model.summary())