from django.utils.text import slugify
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image',blank=True,default="download.png")

    def __str__(self):
        return self.user.username

    def get_slug(self):
        return slugify(self.user.username)

    def has_review(self):
        if self.review_set.all().count == 0:
            return False
        return True

@receiver(post_save,sender = User)
def update_user_profile(sender, instance , created , **kwargs):
    if created and (User.is_staff!= True):
        Profile.objects.create(user = instance)
        instance.profile.save()

class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save,sender = User)
def update_user_admin(sender,instance,created,**kwargs):
    if created and (User.is_staff == True):
        Admin.objects.create(user = instance)
        instance.admin.save()


