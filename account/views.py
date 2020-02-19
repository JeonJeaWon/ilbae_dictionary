from django.shortcuts import render

# Create your views here.


#회원가입
def signup(request):
    return render(request, 'accounts/signup.html')

#로그인
def login(request):
    return render(request, 'accounts/login.html')