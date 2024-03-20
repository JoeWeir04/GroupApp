from django.urls import path
from MVapp import views
app_name = 'MVapp'

urlpatterns = [
path('', views.index, name='index'),
path('about/',views.about,name='about'),
path('register/',views.register,name='register'),
path('genre/<slug:genre_name_slug>/',views.show_genre, name='show_genre'),
path('add_genre/', views.add_genre, name='add_genre'),
path('genre/<slug:genre_name_slug>/add_song/',views.add_song, name='add_song'),
path('login/',views.user_login,name='login'),
path('logout/',views.user_logout,name='logout'),
path('search/', views.search_results, name='search_results'),
path('song/<int:song_id>/comment/', views.comment_for_song, name = 'comment_for_song'),
]
