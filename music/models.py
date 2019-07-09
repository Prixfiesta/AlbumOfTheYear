from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Artist(models.Model):
    artist_name = models.CharField(max_length=40,blank = False,null=False)
    website = models.URLField(max_length=100)
    image = models.ImageField(upload_to='artist-image',blank=True,default="download.png")

    def __str__(self):
        return self.artist_name

    def get_slug(self):
        return slugify(self.artist_name)

    def get_absolute_url(self):
        return reverse('music:artistpage',kwargs={'slug':self.get_slug()})

class Album(models.Model):
    album_name = models.CharField(max_length=50,blank = False,null=False,unique=True)
    avg_rating = models.SmallIntegerField(default=0)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    release_date = models.DateField(blank=False,null  = False)
    added_on = models.DateTimeField(default=timezone.now())
    image = models.ImageField(upload_to='album-image',blank=True,default="download.png")

    def __str__(self):
        return self.album_name

    def get_slug(self):
        return slugify(self.artist)+"-to-"+slugify(self.album_name)

    def get_absolute_url(self):
        return reverse('music:albumpage',kwargs={'slug':self.get_slug(),'pk':self.pk})

    def getratingcount(self):
        return self.review_set.all().count()

