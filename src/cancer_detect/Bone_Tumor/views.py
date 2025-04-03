from django.shortcuts import render
from .models import BoneCell

def index(request):
    cells = BoneCell.objects.all()
    # Giả sử cells là một danh sách các tế bào
    cells = ["Cell 1", "Cell 2", "Cell 3"]
    return render(request, 'Bone_Tumor/index.html', {'cells': cells})

def update(request):
    return render(request, 'Bone_Tumor/update.html')