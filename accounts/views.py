from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserCreationForm,
)
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
)
from django.views.decorators.http import (
    require_POST,
    require_http_methods,
)
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def login(request):
    return render(request, "accounts/login.html")


def logout(request):
    return redirect("/")


def delete(request):
    pass


def update(request):
    pass


def change_password(request):
    pass