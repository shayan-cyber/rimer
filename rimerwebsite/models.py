from django.db import models

# Create your models here.

class Poem(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    content =  models.TextField(blank=True)
    author = models.TextField()
    timeStamp = models.DateTimeField()
    image = models.ImageField(upload_to='poem', default="")
    
    
    def __str__(self):
        return self.title


class Album(models.Model):
    sno = models.AutoField(primary_key=True)
    album_title = models.CharField(max_length=300)
    description =  models.TextField(blank=True)
    album_art = models.ImageField(upload_to='album', default="")
    slug = models.CharField(max_length=150)
    timeStamp = models.DateTimeField()
    def __str__(self):
        return self.album_title

class Song(models.Model):
    sno = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=300)
    mp3 = models.FileField(upload_to='album/mp3', default="")
    thumbnail = models.ImageField(upload_to='album', default="")
    timeStamp = models.DateTimeField()
    def __str__(self):
        return self.song_title


