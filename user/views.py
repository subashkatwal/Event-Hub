from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Passwords must match
        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        # Username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists! Try another.')
            return redirect('register')

        # Email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered! Try logging in.')
            return redirect('register')

        # Create user
        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')

    return render(request, 'user/register.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}! Login successful.')
            return redirect('home')  # make sure 'home' exists in urls.py
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  # reload login page

    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('home')
