from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required
def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """A view that returns a login page and handles the logic for logins"""

    """If the user is logged in, redirect them to the index page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(request.POST['username'],
                                     password=request.POST['password'])
     
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in")
            else:
                login_form.add_error(None, "Your username or password are incorrect")

    else:
        login_form = UserLoginForm()

    return render(request, 'login.html', {'login_form': login_form})


def register(request):
    """A view that returns the registration page and handles the logic for registration"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)

        if register_form.is_valid():
            register_form.save()

            user = auth.authenticate(username=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time!")
    else:
        register_form = UserRegistrationForm()

    return render(request, 'register.html', {'register_form': register_form})


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'profile': user})
