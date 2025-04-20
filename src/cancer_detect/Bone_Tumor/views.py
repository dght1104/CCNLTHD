from django.shortcuts import render
import os
from django.shortcuts import render
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np

# Load mô hình khi server khởi động
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'Bone_Tumor', 'models', 'segnet_model.h5')
model = load_model(MODEL_PATH)

def index(request):
    return render(request, 'Bone_Tumor/index.html')

def update(request):
    return render(request, 'Bone_Tumor/update.html')

def predict(request):
    result = None
    if request.method == "POST" and 'image' in request.FILES:
        image = request.FILES['image']
        
        # Lưu tạm ảnh vào disk
        image_path = os.path.join(BASE_DIR, 'cancer_app', 'temp.jpg')
        with open(image_path, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)

        # Load và xử lý ảnh
        img = load_img(image_path, target_size=(224, 224))  # chỉnh lại nếu model bạn cần size khác
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Dự đoán
        prediction = model.predict(img_array)
        result = "Ung thư" if prediction.argmax() == 1 else "Không ung thư"
    
    return render(request, 'predict.html', {'result': result})