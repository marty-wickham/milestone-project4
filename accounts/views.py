from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    """A view that returns the registration page and handles the logic for registration"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            # username = register_form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        register_form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'register_form': register_form})


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/profile.html', context)
