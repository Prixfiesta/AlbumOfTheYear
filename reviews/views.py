from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,render_to_response
from django.views import generic
from django.template import RequestContext
from django.urls import reverse_lazy
from . import models
from . import forms
# Create your views here.

class ReviewDetail(generic.DetailView):
    model = models.Review

def add_review(request,album_id):
    album = models.Album.objects.get(pk=album_id)
    if request.method == 'POST':
        form = forms.ReviewForm(request.user,album,request.POST)
        if form.is_valid():
            form.save()
            return redirect(album)
    else :
        form = forms.ReviewForm(request.user,album)
    return render(request,'reviews/review_form.html',{'form':form,'album':album,'user':request.user})