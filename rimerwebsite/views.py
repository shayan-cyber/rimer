from django.shortcuts import render ,HttpResponse
from .models import Poem,Album,Song

#send mail module
from django.core.mail import send_mail

# Create your views here.
def home(request):
    poems = Poem.objects.all().order_by('-timeStamp')
    songs = Song.objects.all().order_by('-timeStamp')
    #print(songs)
    albums = Album.objects.all().order_by('-timeStamp')
    first_album = albums.first()
    songs_album = Song.objects.filter(album=first_album)
    #print(songs_album)
    #print(first_album)
    first_song = songs_album.first()


    context = {"poems": poems, "songs": songs, "songs_album": songs_album, "first_album": first_album, "first_song":first_song}
    return render(request,'index.html',context)

def songs(request):
    poems = Poem.objects.all().order_by('-timeStamp')
    songs = Song.objects.all().order_by('-timeStamp')
    #print(songs)
    albums = Album.objects.all().order_by('-timeStamp')
    first_album = albums.first()
    songs_album = Song.objects.filter(album=first_album)
    #print(songs_album)
    #print(first_album)
    first_song = songs_album.first()


    context = {"poems": poems, "songs": songs, "songs_album": songs_album, "first_album": first_album, "first_song":first_song}
    return render(request,'songs.html',context)

def albums(request):
    albums = Album.objects.all().order_by('-timeStamp')
    #print(albums)
    
    context = {"albums":albums}
    return render(request,'albums.html',context)


def search_albums(request):
    query = request.GET['query']
    if len(query)>140:
        albums = Album.objects.none()
    else:
        allPoststitle = Album.objects.filter(album_title__icontains=query)
        allPostscontent = Album.objects.filter(description__icontains=query)
        albums = allPoststitle.union(allPostscontent)
        
    params = {'albums':albums, 'query': query}
    return render(request,'search_albums.html',params)
    #return HttpResponse('this is search')

def search_songs(request):
    query = request.GET['query']
    if len(query)>140:
        songs = Song.objects.none()
    else:
        allPoststitle = Song.objects.filter(song_title__icontains=query)
        #allPoststitle1 = Album.objects.filter(album_title__icontains=query)
        #query2 = allPoststitle1.first().album_title
        #allPostscontent = Song.objects.filter(album__icontains= query2)
        songs = allPoststitle
        
    params = {'songs':songs, 'query': query}
    return render(request,'search_songs.html',params)
    #return HttpResponse('this is search')

def search_poems(request):
    query = request.GET['query']
    if len(query)>140:
        poems = Poem.objects.none()
    else:
        allPoststitle = Poem.objects.filter(title__icontains=query)
        #allPoststitle1 = Album.objects.filter(album_title__icontains=query)
        #query2 = allPoststitle1.first().album_title
        #allPostscontent = Song.objects.filter(album__icontains= query2)
        poems = allPoststitle
        
    params = {'poems':poems, 'query': query}
    return render(request,'search_poems.html',params)
    #return HttpResponse('this is search')
    



def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        #subject = request.POST['subject']
        message = request.POST['message']
        string = "Hey!! " + name + ","  " Your Message Sent Successfully ..We Will Respond  ASAP.."
        #send an email
        send_mail(
            name,#subject
            message,#message
            email,#from email
            ['debroyshayan@gmail.com'],#to email
        )

        return render(request, 'contact.html',{'name':name,'string':string})

    else:
        return render(request, 'contact.html')

def poems(request):
    poems = Poem.objects.all().order_by('-timeStamp')
    context={"poems":poems}
    return render(request, 'poems.html',context)

def about(request):
    return render(request,'about-us.html')




