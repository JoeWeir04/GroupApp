from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import redirect
from django.urls import reverse
from MVapp.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from MVapp.models import Song,Genre
from MVapp.forms import SongForm,GenreForm
from django.db.models import Q


# Create your views here.

def index(request):
    context_dict = {}
    genre_list = Genre.objects.order_by('-likes')[:5]
    songs_list = Song.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['genres'] = genre_list
    context_dict['songs'] = songs_list
    
    response = render(request, 'MVapp/index.html', context=context_dict)
    return response


def about(request):
    context_dict = {}
    response = render(request, 'MVapp/about.html', context=context_dict)
    return response

@login_required
def add_song(request, genre_name_slug):
    try:
        genre = Genre.objects.get(slug=genre_name_slug)
    except Genre.DoesNotExist:
        genre = None

    if genre is None:
        return redirect('/MVapp/')

    form = SongForm()
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            if genre:
                song = form.save(commit=False)
                song.genre = genre
                #song.artist = request.user.userprofile.artistName   
                song.views = 0
                song.save()

                return redirect(reverse('MVapp:show_genre',
                                        kwargs={'genre_name_slug':genre_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form':form,'genre':genre}
    return render(request, 'MVapp/add_song.html',context_dict)

@login_required
def add_genre(request):
    form = GenreForm()
    if request.method == 'POST':
        form = GenreForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/MVapp/')
        else:
            print(form.errors)
    return render(request, 'MVapp/add_genre.html',{'form':form})


def show_genre(request, genre_name_slug):
    context_dict = {}
    try:
        genre = Genre.objects.get(slug=genre_name_slug)
        songs = Song.objects.filter(genre=genre)
        context_dict['songs'] = songs
        context_dict['genre'] = genre
    except Genre.DoesNotExist:
        context_dict['songs'] = None
        context_dict['genre'] = None

    return render(request,'MVapp/genre.html', context=context_dict)

def show_song(request, song_name_slug):
    context_dict = {}
    try:
        song = Song.objects.get(slug=song_name_slug)
        context_dict['song'] = song
    except Song.DoesNotExist:
        context_dict['song'] = None

    return render(request,'MVapp/song.html', context=context_dict)


def search_results(request):

    if request.method == "POST":
        query = request.POST.get('q', '')
        songs = Song.objects.filter(title__contains=query)
        return render(request, 'MVapp/search_songs.html', {'query' :query, 'songs' : songs})
    else:
        return render(request, 'MVapp/search_songs.html',{})



