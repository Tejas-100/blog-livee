from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    return render(request, 'base.html')


@login_required(login_url='login')
def s(request):
    return render(request, 'index.html')


def x(request):
    return render(request, 'index1.html')


def y(request):
    return render(request, 'index2.html')


def z(request):
    return render(request, 'index3.html')


def zz(request):
    return render(request, 'index4.html')


def ab(request):
    return render(request, 'index5.html')


def bc(request):
    return render(request, 'index6.html')


def cd(request):
    return render(request, 'index7.html')


def de(request):
    return render(request, 'index8.html')


def ef(request):
    return render(request, 'index9.html')


def fg(request):
    return render(request, 'index10.html')


def gh(request):
    return render(request, 'index11.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created succesfully for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/mainpage')
        else:
            messages.info(request, 'Username or Password is incorrect!')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')