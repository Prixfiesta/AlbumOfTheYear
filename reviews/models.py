from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.db.models import Avg,Func
from users.models import Profile
from music.models import Album

# Create your models here.

choice = [(x,str(x)) for x in range(101)]
choice.insert(0,(None,'None'))

class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 2)'

class Review(models.Model):
    rating = models.SmallIntegerField(choices=choice,blank=False,null=True)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)

    def get_slug(self):
        return slugify(self.album)+"-review-by-"+self.user.user.username

    def __str__(self):
        return "Album "+self.album.album_name+" rated "+str(self.rating)+" by "+self.user.user.username

    def get_absolute_url(self):
        return reverse('review:reviewdetail',kwargs={'slug':self.get_slug()})

    def save(self,*args,**kwargs):
        super(Review,self).save(*args,**kwargs)
        album_obj = self.album
        print(album_obj.review_set.aggregate(rounded_avg_rating=Round(Avg('rating'))))
        album_obj.avg_rating = album_obj.review_set.aggregate(rounded_avg_rating=Round(Avg('rating')))['rounded_avg_rating']
        album_obj.save()

@receiver(post_delete,sender=Review)
def updateAverageRating(sender,instance,**kwargs):
    if instance.album.review_set.count() == 0:
        instance.album.avg_rating = 0
        instance.album.save()

    else:
        instance.album.avg_rating =  instance.album.review_set.aggregate(rounded_avg_rating=Round(Avg('rating')))['rounded_avg_rating']
        instance.album.save()