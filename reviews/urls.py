from django.urls import re_path
from . import views
app_name='review'

urlpatterns = [
    re_path(r'^(?P<pk>\d+)-(?P<slug>[-\w]+)/$', views.ReviewDetail.as_view(), name='reviewdetail'),
    re_path(r'^reviewit/(?P<album_id>\d+)/$',views.add_review,name='reviewcreate'),

]