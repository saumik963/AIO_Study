from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from Posts.models import Post

User = get_user_model()

# Create your views here.


def signup(request):
    if not request.user.is_authenticated:

        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successuflly')
                form.save()
                # print(form.cleaned_data)
                return redirect("login")

        else:
            form = RegisterForm()
            # print(form)
        return render(request, 'signup.html', {'form': form, "sup_act": "active"})
    else:
        return redirect("profile")


def signin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)

                if user is not None:
                    login(request, user)
                    return redirect('profile')

        else:
            form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form, "sin_act": "active"})
    else:
        return redirect("profile")


def profile(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(user=request.user)
        dp_url = None

        if request.user.dp:  # Check if dp field has a file associated with it
            dp_url = request.user.dp.url
            print(dp_url)

        context = {
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'bio': request.user.bio,
            'dp': dp_url,
            'posts': posts,
            "pro_act": "active"
        }

        return render(request, 'profile.html', context)
    else:
        return redirect("login")


def user_logout(request):
    logout(request)
    return redirect("login")


def pass_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)

        return render(request, 'passchange.html', {'form': form})
    else:
        return redirect('login')


def changeData(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            form = ChangeUserData(
                request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account update successuflly')
                form.save()
                print(form.cleaned_data)
                return redirect("profile")
        else:
            form = ChangeUserData(instance=request.user)
            # print(request.user.email)
        context = {
            "username": request.user.username,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
            'bio': request.user.bio,
            'form': form,
        }
        print(context)
        return render(request, 'update_info.html', context)
    else:
        return redirect("profile")
