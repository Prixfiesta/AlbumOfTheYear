from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from . import models,forms
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()
class ArtistCreateView(LoginRequiredMixin,generic.CreateView):
    model = models.Artist
    template_name = 'music/artist_form.html'
    fields = ('artist_name','website')
    success_url = reverse_lazy('music:artistlist')

class ArtistList(generic.ListView):
    model = models.Artist

class AlbumList(generic.ListView):
    model =models.Album

class ArtistDetail(generic.DetailView):
    model = models.Artist


class AlbumCreateView(generic.CreateView,LoginRequiredMixin):
    form_class = forms.AlbumCreateForm
    template_name = 'music/album_form.html'
    success_url = reverse_lazy('music:albumlist')


class AlbumDetail(generic.DetailView):
    model = models.Album

class BestAlbumList(generic.ListView):
    model = models.Album

    ordering = ['-avg_rating']

class AlbumReviewView(generic.DetailView):
    model = models.Album
    template_name = 'music/album_reviews.html'