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

from django.db.models import Count, Sum


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
            return redirect('summary')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'optifolio/login.html', context)    


def logoutUser(request):
    logout(request)
    return redirect('homepage')


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



@unauthenticated_user
def homepage(request):
    
    context = {}
    return render(request, 'optifolio/homepage.html', context)


@login_required(login_url='homepage')
@admin_only
def dashboard(request):
    
    context = {}
    return render(request, 'optifolio/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id = pk)

    context = {'customer':customer,}
    return render(request, 'optifolio/customer.html',context)

##################################

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def visualisationPage(request):

    visdata = VisData.objects.all()

    return render(request, 'optifolio/visualisationpage.html', {'visdata':visdata})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def summaryPage(request):
    visdata = VisData.objects.all()
    
    comp_number = visdata.count()

    shares_num = visdata.aggregate(Sum(('shares_number')))
    shares_num_sum = (shares_num['shares_number__sum'])

    profit_earned = visdata.aggregate(Sum(('course')))
    profit_sum = ("%.3f" % profit_earned['course__sum'])
    
    
    context = {'comp_number': comp_number, 'shares_num':shares_num_sum, 'profit_earned': profit_sum,}
    return render(request, 'optifolio/summary.html',context)

def pie_chart(request):
    labels = []
    data = []

    visdata_trans = VisData.objects.order_by('title')
    for stock in visdata_trans:
        if stock.shares_number > 0 :
            labels.append(stock.name)
            data.append(stock.shares_number)

    return render(request, 'chart.html', {
        'labels': labels,
        'data': data,
    })

def transaction_val(request):
    transaction = VisData.objects.all()
    money_spent = 0
    for stock in transaction:
        if stock.buy_sell == "+":
            money_spent += stock.course*stock.shares_number + stock.fare
        elif stock.buy_sell == "-":
            money_spent -= stock.course*stock.shares_number 
            money_spent += stock.fare
    return money_spent





    
    


