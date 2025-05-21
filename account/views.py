from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .templates.account import *
from .forms import *
from django.contrib.auth.models import User
from category.models import *

from category.models import Category


def register_view(request):
    if(request.method=='POST'):
        form=RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login_view')
    else:
        form=RegisterForm()
    return render(request,'account/registerForm.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home_view')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login_view')

@login_required
def home_view(request):
    categories=Category.getall()
    context={'categories':categories}
    return render(request, 'category/category_list.html',context)