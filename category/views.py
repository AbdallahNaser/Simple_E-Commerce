from django.shortcuts import render,redirect

from .models import Category


def category_list(request):
    context = {'categories': Category.getall()}
    return render(request, 'category/category_list.html',context)

def category_details(request, id):
    context = {'category': Category.get_single_category(id)}
    return render(request, 'category/category_show.html',context)


def category_delete(request, id):
    Category.delete_single_category(id)
    return redirect('category:category_list')


def category_add(request):
    if(request.method=='POST'):
        name = request.POST.get('category_name')
        description = request.POST.get('category_description')
        Category.objects.create(
            name=name,
            description=description
        )
        return redirect('category:category_list')
    return render(request, 'category/category_insert.html')


