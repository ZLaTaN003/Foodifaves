from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from . forms import RegisterForm,ProfileUpdate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from . models import Profile
# Create your views here.


def register(request):
    if request.method=="POST":
    
     form = RegisterForm(request.POST)
     if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request,f"{username} hello")
        
        return HttpResponseRedirect(reverse("login"))
    else:
       form = RegisterForm()
    return render(request,'users/register.html',{
        "form": form,
        
    })


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileUpdate(instance=request.user.profile)

    
    return render(request, 'users/profile.html', {'form': form})
