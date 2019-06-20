from django.shortcuts import render,redirect
from .forms import SignupForm
from . import models
from django.views import generic

def signup(request):
    if request.method=="POST":
        form =  SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})

class UserView(generic.DetailView):
    model = models.Profile
