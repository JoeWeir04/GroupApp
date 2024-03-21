from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Genre(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)
    

    class Meta:
        verbose_name_plural = 'Genre'
    def __str__(self):
        return self.name
    
    
    
class Song(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    slug = models.SlugField(unique=True)
    artist = models.CharField(max_length = 200,blank = True)
    isExplicit = models.BooleanField(default=False)

    def save(self, *args, **kwargs):  
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Song.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
   

class UserProfile(models.Model):
    ARTIST_LENGTH = 200
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isArtist = models.BooleanField(default=False)
    isMature = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    artistName = models.CharField(max_length=ARTIST_LENGTH, blank=True,help_text = "Only required if creating an Artist Account",)

    

    def save(self, *args, **kwargs):
        if self.isArtist:
            # If the user is an artist, populate artistName
            if not self.artistName:
                self.artistName = self.user.username  # Or any other default value
        else:
            # If the user is not an artist, make sure artistName is blank
            self.artistName = ""
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
    

class Comment(models.Model):
    song=models.ForeignKey(Song,related_name='comments',on_delete=models.CASCADE)
    commenter = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created'])]

        def __str__(self):
            return f'Comment by {self.commenter} on {self.song}'
