import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'GroupApp.settings')
import django
django.setup()
from MVapp.models import Genre,Song

def populate():
    pop_songs = [
        {'title':'Somebody that I used to know',
         'url':'https://www.youtube.com/embed/8UVNT4wvIGY?si=VGn7y449ib9CW_M-','views':12},
         {'title':'All star',
          'url':'https://www.youtube.com/embed/L_jWHffIx5E?si=8uwjYpApVk_6X4o5','views':10},
          {'title':'Yellow',
           'url':'https://www.youtube.com/embed/yKNxeF4KMsY?si=HV8pRP_8WsCklZeZ','views':128} ]
    rock_songs = [
        {'title':'Its my life',
         'url':'https://www.youtube.com/embed/vx2u5uUu3DE?si=xJG8AdeEbha9LYN5','views':1},
        {'title':'Thunder Struck',
          'url':'https://www.youtube.com/embed/v2AC41dglnM?si=cO6A9Kg3TfZHHrbW" allowfullscreen></iframe>','views':9},
        {'title':'Black Betty',
         'url':'https://www.youtube.com/embed/I_2D8Eo15wE?si=nyFMtYux8oGJ_ah7" allowfullscreen></iframe>','views':90} ]
    
    rap_songs = [
        {'title':'GUV NOR',
         'url':'https://www.youtube.com/embed/WW-9TcDTKa8?si=KgApBDUsw8H8ZfaG','views':96},
         {'title':'Shadow Boxing',
          'url':'https://www.youtube.com/embed/dX-2IiYkm1M?si=qe_-NxOjKbRThhH_','views':80} ]
    
    gens = {'Pop': {'songs': pop_songs,"views":128,"likes":64},
            'Rock':{'songs': rock_songs,"views":64,"likes":32},
            'Rap':{'songs':rap_songs, "views":32,"likes":16 }}
    
    for gen, gen_data in gens.items():
        g = add_gen(gen,gen_data["views"],gen_data["likes"])
        for s in gen_data['songs']:
            add_song(g, s['title'], s['url'],s['views'])

    for g in Genre.objects.all():
        for s in Song.objects.filter(genre=g):
            print(f'- {g}: {s}')

def add_song(gen, title, url, views=0):
    s = Song.objects.get_or_create(genre=gen, title=title)[0]
    s.url=url
    s.views=views
    s.save()
    return s 

def add_gen(name,views=0,likes=0):
    g = Genre.objects.get_or_create(name=name)[0]
    g.views = views
    g.likes = likes
    
    g.save()
    return g

if __name__ == '__main__':
   print('Starting Rango population script...')
   populate()

    
    