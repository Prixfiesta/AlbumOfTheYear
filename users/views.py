from django.shortcuts import render,redirect
from .forms import SignupForm,UserProfileForm
from . import models
from django.views import generic

def signup(request):
    if request.method=="POST":
        form =  SignupForm(request.POST)
        pform = UserProfileForm(request.POST)
        if form.is_valid() and pform.is_valid():
            user = form.save()
            profile = pform.save(commit=False)
            profile.user = user
            profile.refresh_from_db()
            user.refresh_from_db()
            profile.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            return redirect('login')
    else:
        form = SignupForm()
        pform = UserProfileForm()
    return render(request,'signup.html',{'form':form,'pform':pform})

class UserView(generic.DetailView):
    model = models.Profile
