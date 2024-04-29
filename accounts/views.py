from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render


def login_view(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("teams_list")
        else:
            messages.error(request, "Failed to login. Try again")
            return redirect("login_view")
    return render(request, "registration/login.html", {})


def logout_view(request):
    logout(request)
    return redirect("login_view")
