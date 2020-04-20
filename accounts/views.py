from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required


def register(request):
    """A view that returns the registration page and handles the logic for registration"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        register_form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'register_form': register_form})


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    return render(request, 'accounts/profile.html')
