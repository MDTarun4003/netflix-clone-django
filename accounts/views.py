from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth, messages

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')

    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == "POST":
        user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'accounts/login.html')


def logout_view(request):
    auth.logout(request)
    return redirect('login')