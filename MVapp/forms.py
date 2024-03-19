from django import forms
from MVapp.models import Genre, Song
from django.contrib.auth.models import User
from MVapp.models import UserProfile


class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=Genre.NAME_MAX_LENGTH,
                           help_text="Please enter the genre name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
    slug = forms.CharField(widget=forms.HiddenInput(), required = False)

    class Meta:
        model = Genre
        fields = ('name',)


class SongForm(forms.ModelForm):
    title = forms.CharField(max_length=Song.TITLE_MAX_LENGTH,
                            help_text="Please enter the title of the song.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the youtube embed URL of the song's music video.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    artist = forms.CharField(max_length=200,
                         help_text="Please enter the artist name")


    class Meta:
        model = Song
        exclude = ('genre',)


   

 

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')
    
    
class UserProfileForm(forms.ModelForm):
        
    isArtist = forms.BooleanField(label="Do you want to create an artist account?", required=False)
    artistName = forms.CharField(label="Artist Name",required=False,help_text="Only required if creating an Artist Account.")
    class Meta:
        model = UserProfile
        fields = ('website','picture','isArtist','artistName')

