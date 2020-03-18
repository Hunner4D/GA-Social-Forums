from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm




def registerUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Congrats {username} on your new account!')
            return redirect('blog-home')

    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form': form})

def viewProfile(request):
    return render(request,'users/profile.html')