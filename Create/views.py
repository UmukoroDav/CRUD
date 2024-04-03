from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .form import Signupform, AddRecord
from django.contrib import messages


# Create your views here.
def base(request):
    return render(request, 'base.html')


def register(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have Successfully been Registered')
            return redirect('apphome')
    else:
        form = Signupform()
        return render(request, 'registration/register.html', {'form':form})
    
    return render(request, 'registration/register.html', {'form     ':form})

def home(request):    
    record = Record.objects.all().order_by('-created_at')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged In!')
            return redirect('apphome')
        else:
            messages.error(request, 'Invalid Email and Password')
            return redirect('apphome')
    else:
        context= {
            'record':record
        }
        return render(request, 'dashboard/home.html', context)


def index(request):
    return render(request, 'dashboard/index.html')

def logout_g(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out!')
    return redirect('apphome')


def record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        context = {
            'record':record
        }
        return render(request, 'dashboard/record.html', context)
    else:
        messages.warning(request, 'You must be logged in...')
        return redirect('apphome')


def delete(request, pk):
    if request.user.is_authenticated:
        delete = Record.objects.get(id=pk)
        delete.delete()
        messages.success(request, 'Your record have been deleted successfully')
        return redirect('apphome')
    else:
        messages.warning(request, 'You must be logged in...')
        return redirect('apphome')

def add_record(request):
    form = AddRecord(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Your Record Is Added Successfully')
                return redirect('apphome')
        return render(request, 'dashboard/add.html', {'form':form})
    else:
        messages.warning(request, 'You must be logged in...')
        return redirect('apphome')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecord(request.POST or None, instance=current_record)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Your Record Is Updated Successfully')
                return redirect('apphome')
        return render(request, 'dashboard/updated.html', {'form':form,})
    else:
        messages.warning(request, 'You must be logged in...')
        return redirect('apphome')