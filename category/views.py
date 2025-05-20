from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.views.generic import *
from .models import Category


class CategoryList(ListView):
    model=Category
    context_object_name = 'categories'
    template_name = 'category/category_list.html'

class CategoryCreate(CreateView):
    model = Category
    fields = ['name','description']
    template_name = 'category/category_insert.html'
    success_url = reverse_lazy('category:category_list')

class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'
    context_object_name = 'category'
    template_name = 'category/category_insert.html'
    success_url = reverse_lazy('category:category_list')


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category/category_show.html'
    context_object_name = 'category'

class CategoryDelete(DeleteView):
    model = Category
    #template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('category:category_list')

"""
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
"""

