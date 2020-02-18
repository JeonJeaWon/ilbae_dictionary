from django.shortcuts import render, get_object_or_404
from .models import Word
# Create your views here.

def home(request):
    words = Word.objects
    return render(request, 'home.html', {'words' : words})

def detail(request, word_id):
    word_detail = get_object_or_404(Word, pk=word_id)
    return render(request, 'detail.html', {'word' : word_detail})