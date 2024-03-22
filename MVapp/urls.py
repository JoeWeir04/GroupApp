from django.urls import path
from MVapp import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'MVapp'

urlpatterns = [
path('', views.index, name='index'),
path('about/',views.about,name='about'),
path('genre/<slug:genre_name_slug>/',views.show_genre, name='show_genre'),
path('add_genre/', views.add_genre, name='add_genre'),
path('genre/<slug:genre_name_slug>/add_song/',views.add_song, name='add_song'),
path('song/<slug:song_name_slug>/',views.show_song,name='show_song'),
path('search/', views.search_results, name='search_results'),
path('song/<int:song_id>/comment/', views.comment_for_song, name='comment_for_song'),
path('register_profile/',views.register_profile,name="register_profile"),
path('like_song/', views.LikeSongView.as_view(), name='like_song'),
path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
path('profiles/',views.ListProfilesView.as_view(), name ='list_profiles'),
path('get_song_views/', views.get_song_views, name='get_song_views'),
path('tags/<slug:tag_slug>/', views.song_list_by_tag, name='song_list_by_tag'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
