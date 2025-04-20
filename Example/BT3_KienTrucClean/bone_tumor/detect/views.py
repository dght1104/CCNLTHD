from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from detect.services.prediction_service import classify_image

def predict_view(request):
    context = {}
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        file_path = fs.path(filename)

        result = classify_image(file_path)
        context['result'] = result
        context['file_url'] = fs.url(filename)

    return render(request, 'result.html', context)
