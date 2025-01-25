from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import LoginForm, RegistrationForm, ForgotPasswordForm
from .models import User

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    # Simulating login; replace with actual Django authentication if using default User
                    request.session['user_id'] = user.id  # Use sessions for login management
                    messages.success(request, "Login successful!")
                    return redirect('home:dashboard')  # Replace 'home' with the name of your main page
                else:
                    messages.error(request, "Invalid username or password.")
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")
    else:
        form = LoginForm()
    
    return render(request, 'login/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login:login')  # Redirect to login page after successful registration
    else:
        messages.error(request, "Registration unsuccessful.")
        form = RegistrationForm()

    return render(request, 'login/register.html', {'form': form})


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(username=username)
                user.password = password  # The `save` method in the model will hash the password
                user.save()
                messages.success(request, "Password updated successfully. You can now log in.")
                return redirect('login')  # Redirect to login page after password reset
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")
    else:
        form = ForgotPasswordForm()

    return render(request, 'forgot_password.html', {'form': form})
