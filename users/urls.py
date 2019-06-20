from django.conf.urls import url
from django.urls import re_path
from . import views
app_name = 'users'
urlpatterns = [
    url(r'^signup/$',views.signup,name='signup'),
    re_path(r'^(?P<pk>\d+)-(?P<slug>[-\w]+)/$',views.UserView.as_view(),name='userdetail'),

]

