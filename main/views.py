from django.shortcuts import render, get_object_or_404
from .models import Character



def index(request):
    return render(request, 'index.html', {'characters': Character.objects.all()})

def character_detail(request, pk):
    return render(request, 'detail.html', {'c': get_object_or_404(Character, pk=pk)})


