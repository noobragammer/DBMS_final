from django.shortcuts import render

def profile_view(request):
    # Example data for the Profile page
    user_data = {
        'first_name': 'Gibe',
        'last_name': 'Bartolome',
        'email': 'bartolome@gmail.com',
        'contact': '09171234567',
        'role': 'Admin',
        'username': 'admin',
        'password': '*******',
        'profile_picture': 'images/profile.png'  # Path to the profile picture
    }

    return render(request, 'inbox/profile.html', {'user': user_data})