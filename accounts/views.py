from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method=='POST':
        # 인증
        return redirect('index')
    else:
        pass
    return render(request, "accounts/signup.html")


def login(request):
    return render(request, "accounts/login.html")


def logout(request):
    return redirect("/")