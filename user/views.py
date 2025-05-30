from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomRegistrationForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def registration_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # নিজের হোম পেজ URL নাম ব্যবহার করো

    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Extra fields Save
            UserProfile.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                age=form.cleaned_data['age'],
                blood_group=form.cleaned_data['blood_group'],
                area=form.cleaned_data['area'],
                phone=form.cleaned_data['phone'],
            )
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
    else:
        form = CustomRegistrationForm()

    return render(request, 'user/registration.html', {'form': form})


@login_required
def profile_view(request):
    messages.info(request, "You must login to continue.")
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'user/profile.html', {'form': form, 'user_profile': user_profile})


