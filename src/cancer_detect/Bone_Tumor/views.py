from django.shortcuts import render
import os
from django.conf import settings
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
from PIL import Image

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

        # Tạo thư mục chứa ảnh tạm nếu chưa tồn tại
        temp_dir = os.path.join(BASE_DIR, 'media')
        os.makedirs(temp_dir, exist_ok=True)

        # Đường dẫn ảnh gốc
        original_image_path = os.path.join(temp_dir, 'uploaded_image.jpg')

        # Lưu ảnh gốc vào thư mục media
        with open(original_image_path, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)

        try:
            # Load ảnh bằng PIL và resize lại ảnh
            img = Image.open(original_image_path)
            img = img.resize((294, 224))  # Resize ảnh thành (294, 224)

            # Chuyển ảnh về dạng array và chuẩn hóa
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            # Dự đoán
            prediction = model.predict(img_array)
            result = "Ung thư" if prediction.argmax() == 1 else "Không ung thư"

            # Save predicted image (Ảnh dự đoán)
            predicted_image_path = os.path.join(temp_dir, 'predicted_image.jpg')
            # Cập nhật ảnh dự đoán (Bạn có thể dùng cách khác để hiển thị ảnh dự đoán)
            img.save(predicted_image_path)

            # Đường dẫn của ảnh gốc và ảnh dự đoán
            image_url = '/media/uploaded_image.jpg'
            predicted_image_url = '/media/predicted_image.jpg'

        except Exception as e:
            result = f"Lỗi xử lý ảnh: {str(e)}"

    return render(request, 'predict.html', {'result': result, 'image_url': image_url, 'predicted_image_url': predicted_image_url})
