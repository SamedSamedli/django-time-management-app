from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser, logout
from . import forms

# from .forms import UserForm


# Create your views here.
from app.forms import TODOForm
from app.models import Blocklist, TODO
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user=user).order_by('priority')
        blocklist = Blocklist.objects.all()
        return render(request, 'index.html', context={'form': form, "blocklist": blocklist , 'todos': todos})


def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context = {
                "form": form
            }
            return render(request, 'login.html', context)


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(request, 'signup.html', context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            user = form.save()
            loginUser(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', context=context)


@login_required(login_url='signup')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("home")
        else:
            return render(request, 'index.html', context={'form': form})


def signout(request):
    logout(request)
    return redirect('login')


# def delete_todo(request, id):
    # TODO.objects.get(pk=id).delete()
    # return redirect('home')


def change_todo(request, id, status):
    todo = TODO.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('home')

@login_required(login_url="login")
def delete_todo(request, id):
        if request.method != 'POST':
            TODO.objects.filter(pk=id).delete()
            return redirect('home')

        else:
            return render(request, 'index.html')


def create_Blocklist(request):
        form2 = forms.CreateBlocklist(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('home')
        else:
            return render(request, 'index.html', context = {'form2': form2})

def delete_blocklist(request, id):
    if request.method == 'GET':
        Blocklist.objects.filter(pk=id).delete()
        return redirect('home')

    else:
        return render(request, 'index.html')