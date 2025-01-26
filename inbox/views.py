from django.shortcuts import render, redirect
from django.contrib import messages
from login.models import User
from django.http import Http404

def profile_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, "You must be logged in to access this page.")
        return redirect('login:login')

    # Fetch the logged-in user's data
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('login:login')
    
    if request.method == "POST":
        # Update user details
        user.first_name = request.POST.get("first_name", user.first_name)
        user.last_name = request.POST.get("last_name", user.last_name)
        user.email_address = request.POST.get("email_address", user.email_address)
        user.contact_number = request.POST.get("contact_number", user.contact_number)
        user.username = request.POST.get("username", user.username)

        # Handle password update
        new_password = request.POST.get("password")
        if new_password and new_password != "*******":  # If the password was changed
            user.password = new_password  # The `save` method will hash the password

        # Save updated user data
        try:
            user.save()
            messages.success(request, "Profile updated successfully.")
        except Exception as e:
            messages.error(request, f"Error updating profile: {e}")

        return redirect('inbox:profile')

    return render(request, 'inbox/profile.html', {"user": user})
