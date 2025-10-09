from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product


# 🏠 Home page view
def home_view(request):
    return render(request, 'app/home.html')


# ➕ Create a new product
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-detail')
    context = {'form': form}
    return render(request, 'app/product_form.html', context)


# 📋 List all products
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'app/product_list.html', {'products': products})


# ✏️ Update a product
def product_update_view(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-detail')
    return render(request, 'app/product_form.html', {'form': form})


# ❌ Delete a product
def product_delete_view(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product-detail')
    return render(request, 'app/product_cd.html', {'product': product})
