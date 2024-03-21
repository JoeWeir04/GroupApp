from django.contrib import admin
from MVapp.models import Genre,Song,Comment

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['song','commenter','body','created']

admin.site.register(Genre, GenreAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Comment,CommentAdmin)
