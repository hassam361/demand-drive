from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate 
from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    form = UserRegisterForm(request.POST)
    
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Your account has been created! You are now able to log in')
        return redirect('home')
    
    return render(request,'users/register.html', {'form':form})