from django.shortcuts import render,redirect
from .forms import RegistrationForm,ProfileForm,UserUpdateForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

def signUp(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)     
            messages.success(request,"Your account has been created successfully")  
            return redirect('index') 

    return render(request,'registration/signup.html',{'form':form})   

@login_required
def profileUpdate(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance = request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request,"Profile has been updated successfully")

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    context = {'user_form': user_form, 'profile_form': profile_form}

    return render(request, 'registration/profile_update.html', context)
