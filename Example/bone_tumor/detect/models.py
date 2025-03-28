from django.db import models

class UploadedImage(models.Model):
    """Lưu trữ ảnh tải lên và kết quả dự đoán."""
    image = models.ImageField(upload_to="uploads/")
    prediction = models.CharField(max_length=20, blank=True, null=True)  # "Benign" hoặc "Malignant"
    confidence = models.FloatField(blank=True, null=True)  # Độ chính xác mô hình (%)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image.name} - {self.prediction} ({self.confidence:.2f}%)" if self.prediction else self.image.name