import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'GroupApp.settings')
import django
django.setup()
from django.contrib.auth.models import User
from MVapp.models import Genre,Song,UserProfile

def populate():
    def add_user_profile(user):
        profile = UserProfile.objects.create(user=user)
    
        profile.isArtist = True
        profile.isMature = False 
        profile.artistName = f"{user.username}'s Artist Name" 
    
        # Save the profile
        profile.save()

    def add_user(username, password, email):
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()  # Save the created user object to the database
        return user

    users = [
        {'username': 'Mark', 'password': 'password1', 'email': 'user1@example.com'},
        {'username': 'musicLover555', 'password': 'password2', 'email': 'user2@example.com'},
        {'username': 'ILoveMusicLover555', 'password': 'password3', 'email': 'user3@example.com'},
        {'username': 'Drake', 'password': 'password3', 'email': 'user3@example.com'},
        {'username': 'MarkFan', 'password': 'password3', 'email': 'user3@example.com'}
    ]

    for user_data in users:
        user = add_user(user_data['username'], user_data['password'], user_data['email'])
        add_user_profile(user)
        

    

        
    pop_songs = [
        {'title':'Somebody that I used to know',
         'url':'https://www.youtube.com/embed/8UVNT4wvIGY?si=VGn7y449ib9CW_M-','views':12,'likes':12,'artist':'Gotye'},
         {'title':'All star',
          'url':'https://www.youtube.com/embed/L_jWHffIx5E?si=8uwjYpApVk_6X4o5','views':10,'likes':12,'artist':'Smash Mouth'},
          {'title':'Yellow',
           'url':'https://www.youtube.com/embed/yKNxeF4KMsY?si=HV8pRP_8WsCklZeZ','views':128,'likes':12,'artist':'Coldplay'},
            {'title':'Holding On To You','url':'https://www.youtube.com/embed/ktBMxkLUIwY?si=g1M4MzPScofN297l','views':100,'likes':50,'artist':'Twenty One Pilots'},
            {'title':'On Melancholy Hill','url':'https://www.youtube.com/embed/04mfKJWDSzI?si=kgL74FuQ67lOez1s','views':100,'likes':50,'artist':'Gorillaz'} ]
    rock_songs = [
        {'title':'Its my life',
         'url':'https://www.youtube.com/embed/vx2u5uUu3DE?si=xJG8AdeEbha9LYN5','views':1,'likes':12,'artist':'Bon Jovi'},
         {'title':'I Dont Love you','url':'https://www.youtube.com/embed/pyi0ZfuIIvo?si=t_dpNDVs7mHcEV2-','views':100,'likes':50,'artist':'My Chemical Romance'},
         {'title':'Helena','url':'https://www.youtube.com/embed/UCCyoocDxBA?si=1I7X8aqRPcA3C-xL','views':100,'likes':50,'artist':'My Chemical Romance'},
        {'title':'Thunder Struck',
          'url':'https://www.youtube.com/embed/v2AC41dglnM?si=cO6A9Kg3TfZHHrbW" allowfullscreen></iframe>','views':9,'likes':12,'artist':'AC/DC'},
        {'title':'Black Betty',
         'url':'https://www.youtube.com/embed/I_2D8Eo15wE?si=nyFMtYux8oGJ_ah7" allowfullscreen></iframe>','views':90,'likes':12,'artist':'Ram Jam'} ]
    
    rap_songs = [
        {'title':'GUV NOR',
         'url':'https://www.youtube.com/embed/WW-9TcDTKa8?si=KgApBDUsw8H8ZfaG','views':96,'likes':12,'artist':'MF DOOM'},
         {'title':'Shadow Boxing',
          'url':'https://www.youtube.com/embed/dX-2IiYkm1M?si=qe_-NxOjKbRThhH_','views':80,'likes':12,'artist':'Yung Lean'},
           {'title':'Victim','url':'https://www.youtube.com/embed/HDajKZ3ytdY?si=ftyVYu1Frw4u1j1W','views':1230,'likes':132,'artist':'bladee + Thaiboy Digital + ECCO2K'},
           {'title':'Love Sosa','url':'https://www.youtube.com/embed/YWyHZNBz6FE?si=TOoj1O8wCLOplUJe','views':100,'likes':50,'artist':'Chief Keef','isExplicit':True} ]
    elec_songs =[
        {'title':'Boiler Room Set','url':'https://www.youtube.com/embed/djGlyTcW30Q?si=0P2smZmg-2qss9iA','views':130123,'likes':3550,'artist':'Minna-no-kimochi','isExplicit':True},
        {'title':'California Dream Girl','url':'https://www.youtube.com/embed/7OYveRwPXl8?si=HL9NnbodwcppgP8a','views':1500,'likes':317,'artist':'THE HELPP'},
        {'title':'Silver','url':'https://www.youtube.com/embed/53I6fcFXqxo?si=tVY1YRa0GIHCSdnj','views':10,'likes':5,'artist':'A. G. COOK'},
        {'title':'skyskysky','url':'https://www.youtube.com/embed/J1hSjZNX48I?si=Bmu_4PueUXXXUkBG','views':1239,'likes':120,'artist':'PeterParker69 x Tennyson'},
        {'title':'Something Comforting','url':'https://www.youtube.com/embed/-C-2AqRD8io?si=Ac8EeHm6i8u2LS2D','views':200,'likes':70,'artist':'Porter Robinson'}
        ]
    
    gens = {'Pop': {'songs': pop_songs,"views":128,"likes":64},
            'Rock':{'songs': rock_songs,"views":64,"likes":32},
            'Rap':{'songs':rap_songs, "views":32,"likes":16 },
            'Electronic':{'songs':elec_songs,"views":32,"likes":16}}
    
    for gen, gen_data in gens.items():
        g = add_gen(gen,gen_data["views"],gen_data["likes"])
        for s in gen_data['songs']:
            add_song(g, s['title'], s['url'],s['views'],s['likes'],s['artist'])

    for g in Genre.objects.all():
        for s in Song.objects.filter(genre=g):
            print(f'- {g}: {s}')

def add_song(gen, title, url, views=0,likes=0,artist="",isExplicit=""):
    s = Song.objects.get_or_create(genre=gen, title=title)[0]
    s.url=url
    s.views=views
    s.likes =likes
    s.artist = artist
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

    
    