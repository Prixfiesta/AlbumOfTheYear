from django.urls import re_path
from . import views
app_name='review'

urlpatterns = [
    re_path(r'^(?P<pk>\d+)-(?P<slug>[-\w]+)/$', views.ReviewDetail.as_view(), name='reviewdetail'),
    re_path(r'^reviewit/(?P<album_id>\d+)/$',views.add_review,name='reviewcreate'),
    re_path(r'^changereview/(?P<pk>\d+)-(?P<slug>[-\w]+)/$',views.UpdateReview.as_view(),name='changereview'),
    re_path(r'^deletereview/(?P<pk>\d+)-(?P<slug>[-\w]+)/$',views.DeleteReview.as_view(),name='deletereview'),

]