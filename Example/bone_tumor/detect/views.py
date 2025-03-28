from django.shortcuts import render
from .models import UploadedImage

def upload_image(request):
    """Xử lý tải ảnh lên."""
    if request.method == "POST" and request.FILES.get("image"):
        image_file = request.FILES["image"]
        uploaded_image = UploadedImage.objects.create(image=image_file)

        return render(request, "result.html", {"image": uploaded_image})

    return render(request, "upload.html")