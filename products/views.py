from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.views.decorators.http import (
    require_http_methods, 
    require_POST,
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductForm
from .models import Product


def index(request):
    products = Product.objects.all().order_by("-pk")
    context = {
        "products": products,
    }
    return render(request, "products/index.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
    }
    return render(request, "products/product_detail.html", context)


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


@require_POST
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user.is_staff:
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect("index")
    messages.error(request, "접근이 불가합니다.")
    return redirect("index")


@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user.is_staff:
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                product = form.save()
                return redirect("products:product_detail", product.pk)
        else:
            form = ProductForm(instance=product)
    else:
        messages.error(request, "접근이 불가합니다.")
        return redirect("index")
    
    context = {
        "form": form,
        "product": product,
    }
    return render(request, "products/update.html", context)


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return redirect("products:product_detail", pk)
    return redirect("products:login")