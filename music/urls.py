from django.urls import re_path
from . import views

app_name = 'music'
urlpatterns = [
    re_path(r'^artists/all/$',views.ArtistList.as_view(),name='artistlist'),
    re_path(r'^artists/(?P<pk>\d+)-(?P<slug>[-\w]+)/$',views.ArtistDetail.as_view(),name='artistpage'),
    re_path(r'^albums/create/$',views.AlbumCreateView.as_view(),name='albumcreate'),
    re_path(r'^albums/(?P<pk>\d+)-(?P<slug>[-\w]+)/$',views.AlbumDetail.as_view(),name='albumpage'),
    re_path(r'^artists/create/$',views.ArtistCreateView.as_view(),name='artistcreate'),
    re_path(r'^albums/all/$',views.AlbumList.as_view(),name='albumlist'),
    re_path(r'^albums/best/$',views.BestAlbumList.as_view(),name='bestalbumlist'),
    re_path(r'^albums/(?P<pk>\d+)-(?P<slug>[-\w]+)/reviews/$',views.AlbumReviewView.as_view(),name='albumreview'),


]