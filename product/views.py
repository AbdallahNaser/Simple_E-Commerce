from django.shortcuts import render,redirect
from category.models import Category
from product.models import Product

from .forms import ProductFormModel


def product_list(request):
    context={'products':Product.get_all_products()}
    return render(request, 'product/product_list.html',context)
def product_details(request,id):
    context = {'product': Product.get_single_product(id)}
    return render(request, 'product/product_details.html', context)
def product_delete(request,id):
    Product.delete_single_product(id)
    return redirect('product:product_list')


def product_add(request):
    if request.method == 'POST':
        form = ProductFormModel(request.POST, request.FILES)
        if form.is_bound and form.is_valid():
            form.save()
            return redirect('product:product_list')
    else:
        form = ProductFormModel()
    context = {'AddProduct': form,'categories':Category.getall()}

    return render(request, 'product/product_add.html', context)
''' 
def product_add2(request):
    productForm=ProductFormModel
    context={'categories':Category.getall(),'AddProduct':productForm}


    if(request.method=='POST'):
        name = request.POST.get('product_name')
        description = request.POST.get('description', '')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        status = request.POST.get('status', 'true') == 'true'
        image=request.FILES['product_image']

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock=stock,
            image=image,
            category_id=category.id,
            status=status,
        publish_date="2025-11-11"
        )
        return redirect('product:product_list')

    return render(request,'product/product_add.html', context)

'''
