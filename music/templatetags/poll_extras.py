from django import template
from music.models import Album
from users.models import Profile
# from django.contrib.auth.models import User
register = template.Library()


@register.inclusion_tag('music/songratingbyuser.html')
def getratingofuser(albumpk,user):
    profile_obj = Profile.objects.get(user=user)
    album_obj = Album.objects.get(pk=albumpk)
    rating_obj = Album.objects.get(pk=albumpk).review_set.filter(user=profile_obj).first()
    created = True
    if rating_obj is None:
        created = False

    return {'rating':rating_obj,'created':created,'albumobj':album_obj,'profileobj':profile_obj}