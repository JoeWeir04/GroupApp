from django import template
from MVapp.models import Genre

register = template.Library()

@register.inclusion_tag('MVapp/genres.html')
def get_genre_list(current_genre=None):
    return {'genres': Genre.objects.all(),
            'current_genre':current_genre}