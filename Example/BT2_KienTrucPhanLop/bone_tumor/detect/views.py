from django.shortcuts import render

def upload_image(request):
    """Xử lý tải ảnh lên mà không lưu vào database."""
    if request.method == "POST" and request.FILES.get("image"):
        image_file = request.FILES["image"]  # Lấy file ảnh

        return render(request, "result.html", {"image_url": image_file})

    return render(request, "upload.html")