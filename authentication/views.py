from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Registration view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'authentication/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login after logout

# Home view (protected by login_required)
@login_required
def home(request):
    response = render(request, 'authentication/home.html')
    # Prevent caching of the page
    response['Cache-Control'] = 'no-store'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
