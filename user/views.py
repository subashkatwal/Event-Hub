from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!! Try another?')
            return redirect('register')
        
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')
        
    return render(request, 'user/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('event_list')
        else:
            return render(request, 'user/login.html', {'error': 'Invalid credentials'})
    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')
