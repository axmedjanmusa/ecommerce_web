from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import ProfileUpdateForm, RegistrationForm, LoginForm
from .models import Profile


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            messages.info(request, "You registrated successfully !")
            return redirect('user:login_url')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect('user:registration_url')
    else:
        form = RegistrationForm()

        context = {
            'form': form
        }

        return render(request, 'user/registration.html', context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, "Login successfully !")
                return redirect("home")
            else:
                messages.warning(request, "Login/Password is incorrect !")
                return redirect("login_url")
        else:
            messages.warning(request, "Login/Password is incorrect !")
            return redirect("login_url")
    else:
        form = LoginForm()
        context = {
            'form': form
        }

        return render(request, 'user/login.html', context)


def logout_view(request):
    logout(request)
    messages.info(request, "Logout Successfully !")
    return redirect("home")


def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile, created = Profile.objects.get_or_create(user=user)
    context = {
        'profile': profile,
    }

    return render(request, "user/profile.html", context)


def update_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            messages.success(request, "Профиль успешно обновлён!")
            return redirect("user:profile_view", user_id=user.id)
    else:
        form = ProfileUpdateForm(instance=profile, initial={
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        })

    context = {
        "form": form
    }
    return render(request, "user/update_profile.html", context)