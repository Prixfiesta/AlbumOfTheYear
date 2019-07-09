from django.forms import ModelForm
from . import models
class ReviewForm(ModelForm):
    class Meta:
        model = models.Review
        exclude = ('user','album')

    def __init__(self,user,album,*args,**kwargs):
        self.user = user
        self.album = album
        super(ReviewForm,self).__init__(*args,**kwargs)


    def save(self):
        review = super(ReviewForm,self).save(commit=False)
        review.user = self.user.profile
        review.album = self.album
        review.save()
        return review