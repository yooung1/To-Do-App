from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'todoapp/todo.html', {})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 3:
            messages.error(request, 'Password must be at least 3 characters')
            return redirect('register')
        
        get_all_users_by_username = User.objects.filter(username=username)
        get_all_users_by_email = User.objects.filter(email=email)
        if get_all_users_by_username or get_all_users_by_email:
            messages.error(request, 'Error, Username or Email already exist use another')
            return redirect('register')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
    return render(request, 'todoapp/register.html', {})

def loginPage(request):
    if request.method == "POST":
        username = request.get.POST('uname')
        password = request.get.POST('pass')
    return render(request, 'todoapp/login.html', {})