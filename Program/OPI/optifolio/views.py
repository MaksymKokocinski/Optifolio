from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import CreateUserForm, CustomerForm
from .decorators import unauthenticated_user,allowed_users,admin_only

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'Account was created for'+ username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'optifolio/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'optifolio/login.html', context)    


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):

    context = {}
    return render(request, 'optifolio/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'optifolio/account_settings.html',context)





@login_required(login_url='login')
@admin_only
def home(request):
    
    context = {}
    return render(request, 'optifolio/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id = pk)

    context = {'customer':customer,}
    return render(request, 'optifolio/customer.html',context)





