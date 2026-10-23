from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, StudentProfileForm
from .models import StudentProfile

def home(request):
    return render(request, 'students/home.html')

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        profile_form = StudentProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = RegisterForm()
        profile_form = StudentProfileForm()
    return render(request, 'students/register.html', {'user_form': user_form, 'profile_form': profile_form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'students/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def contact(request):
    return render(request, 'students/contact.html')

def about(request):
    return render(request, 'students/about.html')


