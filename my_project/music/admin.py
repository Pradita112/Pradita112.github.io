from django.contrib import admin
from .models import Album,Buku

# Register your models here.

class AdminAlbum(admin.ModelAdmin):
    pass


admin.site.register(Album,AdminAlbum)

class AdminBuku(admin.ModelAdmin):
    pass

admin.site.register(Buku,AdminBuku)
