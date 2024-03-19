from django.contrib import admin
from MVapp.models import Genre,Song

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Genre, GenreAdmin)
admin.site.register(Song, SongAdmin)
