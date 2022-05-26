from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from users.models import Profile
from django.contrib import messages
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm, InitialUpdate
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

@login_required
def profile(request):
    current_user = request.user
    if not current_user.is_superuser:
        extradata = SocialAccount.objects.filter(user=current_user).first().extra_data
        img = extradata["picture"]
    else:
        img = current_user.profile.image.url
    context = {
        'img':img,
        }
    return render(request, 'users/profile.html', context)

def moderatorprofile(request):
    return render(request, 'users/moderatorprofile.html')

@login_required
def profileupdate(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,   instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile-update.html', context)

def InitialProfileUpdate(request):
    if request.method == 'POST':
        p_form = InitialUpdate(request.POST, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
        return redirect('profile')

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }
    return render(request, 'users/initial.html', context)







