from django.shortcuts import render, get_object_or_404, redirect
from .models import Word
from django.utils import timezone
# Create your views here.

#기본홈페이지
def home(request):
    if request.GET.get('search'):
        result = Word.objects.filter(**{ 'title__contains' : request.GET.get('search')})
        if not result:  #result 리스트가 비었으면
            return render(request, 'home.html', {'empty': '검색 결과가 없습니다'})
        return render(request, 'home.html',{ 'results': result })
    else:
        words = Word.objects
        return render(request, 'home.html', {'words' : words, 'check':'check'})

#게시글 조회
def detail(request, word_id):
    word_detail = get_object_or_404(Word, pk=word_id)
    return render(request, 'detail.html', {'word' : word_detail})

#게시글 추가페이지
def new(request):
    return render(request, 'new.html')

#추가페이지 이용 글 추가
def create(request):
    word = Word()
    word.title = request.GET['title']
    word.body =  request.GET['body']
    word.pup_date =  timezone.datetime.now()
    word.save()
    return redirect('/word/'+str(word.id))

#게시글 삭제
def delete(request, word_id):
    word = get_object_or_404(Word , pk = word_id)
    word.delete()
    return redirect('home')

#게시글 수정 페이지
def edit(request, word_id):
    word_edit = get_object_or_404(Word , pk = word_id)
    return render(request, 'edit.html', {'word' : word_edit})

#수정 페이지 이용 글 수정
def update(request, word_id):
    word = Word.objects.get(pk = word_id)
    word.title = request.POST['title']
    word.body =  request.POST['body']
    word.pup_date =  timezone.datetime.now()
    word.save()
    return redirect('home')

