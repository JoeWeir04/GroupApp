from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.shortcuts import redirect
from django.urls import reverse
from MVapp.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from MVapp.models import Song,Genre, Comment
from MVapp.forms import SongForm,GenreForm, CommentForm
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

def register(request):
    registered = False

    if request.method == 'POST':
        user_form=UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user=user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'MVapp/register.html',context = {"user_form":user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username , password = password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('MVapp:index'))
            else:
                return HttpResponse("Your MVapp account is disabled.")
        else:
            print(f"Invalid login details: {username},{password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'MVapp/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('MVapp:index'))


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


def search_results(request):

    if request.method == "POST":
        query = request.POST.get('q', '')
        songs = Song.objects.filter(title__contains=query)
        return render(request, 'MVapp/search_songs.html', {'query' :query, 'songs' : songs})
    else:
        return render(request, 'MVapp/search_songs.html',{})


@login_required
def comment_for_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.song = song
            comment.author = request.user
            comment.save()
            return redirect('comment_for_song', song_id=song.id)

    else:
        comment_form= CommentForm()
    return render(request, 'song/detail.html', {'song' : song, 'comment_form' : comment_form})

        
    
