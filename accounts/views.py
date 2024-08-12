from django.shortcuts import render, redirect
from .form import SignUp ,User_edit ,Profile_edit
from django.contrib.auth import authenticate ,login
from .models import Profile
from django.urls import reverse
from django.contrib.auth.decorators import login_required 

# Create your views here.


def sign_up(request):
    if request.method=="POST":
        form = SignUp(request.POST )
        if form.is_valid():
            form.save()
            username =form.cleaned_data['username'] 
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form=SignUp()

    
    context={'form':form}
    return render(request,"registration/sign_up.html",context)

@login_required
def profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,"accounts/profile.html",{'profile':profile})

@login_required
def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=="POST":
        userform = User_edit(request.POST,instance=request.user)
        profileform = Profile_edit(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=0)
            myprofile.user=request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = User_edit(instance=request.user)
        profileform = Profile_edit(instance=profile)

    
    return render(request,"accounts/edit.html",{'profile_edit':profileform,'user_edit':userform})