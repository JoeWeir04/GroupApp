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
path('register_profile/',views.register_profile,name="register_profile"),
path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
