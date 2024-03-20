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
    isExplicit = forms.BooleanField(label="Explicit",required=False,help_text="Check this box if the song contains explicit content, such as strong language or mature themes.")
    


    class Meta:
        model = Song
        exclude = ('genre','artist')


   

 

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')
    
    
class UserProfileForm(forms.ModelForm):
    isArtist = forms.BooleanField(label="Do you want to create an artist account?", required=False)
    isMature = forms.BooleanField(label="Mature Account", required=False,help_text="Explicit songs will not be shown to you if your account is not mature")
    artistName = forms.CharField(label="Artist Name",required=False,help_text="Only required if creating an Artist Account.")
    class Meta:
        model = UserProfile
        fields = ('picture','isMature','isArtist','artistName',)

