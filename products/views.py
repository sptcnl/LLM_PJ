from django.shortcuts import (
    render, 
    redirect
)
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request, "products/index.html")


def product_detail(request):
    pass


@login_required
def create(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.save()
                return redirect("index")
        else:
            form = ProductForm()
        context = {"form": form}
        return render(request, "products/create.html", context)
    messages.error(request, "접근이 불가합니다.")
    return redirect("index")


def delete(request):
    pass


def update(request):
    pass