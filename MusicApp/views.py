from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import User, MusicFile


# Create your views here.

def homepage(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('homepage')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        access = request.POST['access']
        allowed_emails = request.POST.getlist('allowed_emails')
        music_file = MusicFile.objects.create(
            uploader=request.user,
            file=file,
            access=access,
            allowed_emails=','.join(allowed_emails),
        )
        return redirect('homepage')
    return render(request, 'upload.html')
