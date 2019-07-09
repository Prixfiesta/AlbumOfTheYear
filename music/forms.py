from django import forms
from .models import Album,Artist

class AlbumCreateForm(forms.ModelForm):

    artist = forms.ModelChoiceField(queryset=Artist.objects.all())

    class Meta:
        model = Album
        fields = ('album_name','artist','release_date','image')
    def save(self, commit=True):
        artist,created = Artist.objects.get_or_create(artist_name=self.cleaned_data['artist'],defaults={'website':''})

        return super(AlbumCreateForm,self).save(commit)
