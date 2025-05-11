from django.shortcuts import render
import os
from django.conf import settings
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
from PIL import Image
import uuid
# Load mô hình khi server khởi động
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'Bone_Tumor', 'models', 'segnet_model.h5')
model = load_model(MODEL_PATH)

def index(request):
    return render(request, 'index.html')

def predict(request):
    result = None
    image_url = None
    predicted_image_url = None

    if request.method == "POST" and 'image' in request.FILES:
        image = request.FILES['image']

        # Tạo thư mục media nếu chưa có
        temp_dir = settings.MEDIA_ROOT
        os.makedirs(temp_dir, exist_ok=True)

        # Tạo tên file ngẫu nhiên để tránh trùng
        original_filename = f"{uuid.uuid4().hex}_uploaded.jpg"
        predicted_filename = f"{uuid.uuid4().hex}_predicted.jpg"

        original_image_path = os.path.join(temp_dir, original_filename)
        predicted_image_path = os.path.join(temp_dir, predicted_filename)

        # Lưu ảnh upload
        with open(original_image_path, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)

        try:
            # Load ảnh và resize
            img = Image.open(original_image_path).convert("RGB")
            img = img.resize((294, 224))

            # Dự đoán
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0
            prediction = model.predict(img_array)

            result = "Ung thư" if prediction.argmax() == 1 else "Không ung thư"

            # Lưu lại ảnh đã resize như ảnh dự đoán (hoặc bạn có thể vẽ mask nếu segmentation)
            img.save(predicted_image_path)

            # Đường dẫn để truyền về template
            image_url = f"{settings.MEDIA_URL}{original_filename}"
            predicted_image_url = f"{settings.MEDIA_URL}{predicted_filename}"

        except Exception as e:
            result = f"Lỗi xử lý ảnh: {str(e)}"

    return render(request, 'predict.html', {
        'result': result,
        'image_url': image_url,
        'predicted_image_url': predicted_image_url
    })