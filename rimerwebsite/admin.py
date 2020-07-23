from django.contrib import admin


from .models import Poem,Album,Song

admin.site.register(Poem)
admin.site.register(Album)
admin.site.register(Song)
