from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import SignupForm

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard_view')

        else:
            return HttpResponse ("<h3 style='text-align: center; color: red; padding-top:40px;'><b>Invalid Credentials.</b> Make sure your Username or Password is correct.</h3>")

    return render(request, "accounts/home.html")

def signup_view(request):
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('login_view')
        
    return render(request, "accounts/signup.html", {"form": form})

def logout_view(request):
    logout(request)

    return redirect('login_view')

def dashboard_view(request):
    if request.user.is_authenticated:
        return render(request, "accounts/dashboard.html")
    else:
        return redirect('login_view')