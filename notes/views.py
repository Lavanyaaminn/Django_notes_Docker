from django.shortcuts import render
from .models import Note

def index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})

def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Note.objects.create(title=title, content=content)
    return render(request, 'notes/add_note.html')
