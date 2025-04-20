import cv2
import numpy as np
from infrastructure.model.cnn_model import predict_image

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def classify_image(image_path):
    image_array = preprocess_image(image_path)
    prediction = predict_image(image_array)
    return "Positive" if prediction[0][0] > 0.5 else "Negative"
