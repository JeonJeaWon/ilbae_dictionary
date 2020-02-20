from django.shortcuts import render, get_object_or_404, redirect
from .models import Word
from django.utils import timezone
# Create your views here.

def home(request):
    words = Word.objects
    return render(request, 'home.html', {'words' : words})

def detail(request, word_id):
    word_detail = get_object_or_404(Word, pk=word_id)
    return render(request, 'detail.html', {'word' : word_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    word = Word()
    word.title = request.GET['title']
    word.body =  request.GET['body']
    word.pup_date =  timezone.datetime.now()
    word.save()
    return redirect('/word/'+str(word.id))

def delete(request, word_id):
    word = get_object_or_404(Word , pk = word_id)
    word.delete()
    return redirect('home')

def edit(request, word_id):
    word_edit = get_object_or_404(Word , pk = word_id)
    return render(request, 'edit.html', {'word' : word_edit})

def update(request, word_id):
    word = Word.objects.get(pk = word_id)
    word.title = request.POST['title']
    word.body =  request.POST['body']
    word.pup_date =  timezone.datetime.now()
    word.save()
    return redirect('home')
