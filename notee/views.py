from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .models import note


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')


@login_required(login_url='login')
def dashboard(request):
    item = note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'dashboard.html', {'item': item})


@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        note.objects.create(Title=title, Description=description, user=request.user)
        return redirect('dashboard')
    return render(request, 'create.html')


@login_required(login_url='login')
def update(request, id):
    item = get_object_or_404(note, id=id, user=request.user)
    if request.method == 'POST':
        item.Title = request.POST.get('title')
        item.Description = request.POST.get('description')
        item.save()
        return redirect('dashboard')
    return render(request, 'update.html', {'item': item})


@login_required(login_url='login')
def delete(request, id):
    item = get_object_or_404(note, id=id, user=request.user)
    item.delete()
    return redirect('dashboard')


def logout_page(request):
    logout(request)
    return redirect('login')
   