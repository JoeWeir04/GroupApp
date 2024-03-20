from django.contrib import admin
from .models import Song, Genre, Comment
# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'views', 'likes', 'slug']

class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'url', 'views']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['song', 'commenter', 'body', 'created']

admin.site.register(Genre, GenreAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Comment, CommentAdmin)
