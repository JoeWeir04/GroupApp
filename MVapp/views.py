from unicodedata import category
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse 
from django.shortcuts import redirect
from django.urls import reverse
from MVapp.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from MVapp.models import Song,Genre,Comment
from MVapp.forms import SongForm,GenreForm,CommentForm
from django.db.models import Q
from django.views import View
from django.contrib.auth.models import User
from MVapp.models import UserProfile
from django.utils.decorators import method_decorator


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
                song.views = 0
                

                user_profile = request.user.userprofile
                song.artist = user_profile.artistName
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
        comments = Comment.objects.filter(song=song)
        context_dict['song'] = song
        context_dict['comments'] = comments
        
        #userProfile = FETCH USER SOMEHOW
        #userProfile.newListen(song)
        
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
    
@login_required
def register_profile(request):
    form = UserProfileForm()

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect(reverse('MVapp:index'))
        else:
            print(form.errors)
    
    context_dict = {'form':form}
    return render(request,'MVapp/profile_registration.html',context_dict)

class ProfileView(View):
    def get_user_details(self,username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'artistName':user_profile.artistName,'picture':user_profile.picture})

        return (user, user_profile, form)

    @method_decorator(login_required)
    def get(self,request,username):
        try:
            (user,user_profile,form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('MVapp:index'))
        
        context_dict = {'user_profile':user_profile,'selected_user':user,'form':form}
        return render(request,'MVapp/profile.html',context_dict)
    
    @method_decorator(login_required)
    def post(self,request,username):
        try:
            (user,user_profile,form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('MVapp:index'))
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('MVapp:profile',user.username)
        else:
            print(form.errors)
        context_dict = {'user_profile':user_profile,'selected_user':user,'form':form}
        return render(request,'MVapp/profile.html',context_dict)
    
class ListProfilesView(View):
    @method_decorator(login_required)
    def get(self,request):
        profiles = UserProfile.objects.all()
        return render(request,'MVapp/list_profiles.html',{'user_profile_list':profiles})
    
@login_required
def comment_for_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.song = song 
            comment.commenter = request.user
            comment.save()
            return redirect('MVapp:show_song', song_name_slug=song.slug)

    else:
        comment_form = CommentForm()

    return render(request, 'MVapp/song.html',{'song':song,'comment_form':comment_form})

class LikeSongView(View):
    @method_decorator(login_required)
    def get(self,request):
        song_id= request.GET['song_id']
        try:
            song=Song.objects.get(id=int(song_id))
        except Song.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        
        song.likes = song.likes + 1
        song.save()

        return HttpResponse(song.likes)



    




