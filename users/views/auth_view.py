from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import User
from users.forms import LoginForm

def login_view(request):
    loginForm = LoginForm()

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                _next = request.GET.get('next')
                if _next is not None:
                    return redirect(_next)
                return redirect('/')
            messages.add_message(request, messages.ERROR, 'Usuário ou senha inválidos', extra_tags='danger')   
            return redirect('/')
    return render(request, 'auth/login.html', {'form': loginForm})

def logout_view(request):
    logout(request)
    return redirect('/auth/login')