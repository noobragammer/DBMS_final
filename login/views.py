from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'login/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()

            # Invalidate all previous sessions for the user
            for session in Session.objects.filter(expire_date__gte=timezone.now()):
                data = session.get_decoded()
                if data.get('_auth_user_id') == str(user.id):
                    session.delete()

            login(request, user)
            return redirect('dashboard')  # Replace with the name of your desired post-login page
    else:
        form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('login')
