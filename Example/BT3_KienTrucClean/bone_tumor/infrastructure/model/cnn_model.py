import tensorflow as tf
from tensorflow.keras.models import load_model

MODEL_PATH = 'infrastructure/model/saved_model.h5'

_model = None

def load_cnn_model():
    global _model
    if _model is None:
        _model = load_model(MODEL_PATH)
    return _model

def predict_image(image_array):
    model = load_cnn_model()
    prediction = model.predict(image_array)
    return prediction
