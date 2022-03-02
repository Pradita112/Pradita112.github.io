from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Album, Buku


# Create your views here.

def index(request):
    return render (request, 'index.html')

class ListAlbumView(View):

    template_name = 'list_album.html'
    
    def get(self, request):
        obj = Album.objects.all() #mengambil semua data album dari db
        print(obj)
        return render(request, self.template_name, {
            "albums": obj,
            "test":"Ngetes",
        })

class listbukuview(View):

    template_name = 'list_buku.html'

    def get(self, request):
        obj = Buku.objects.all()
        print(obj)
        return render(request, self.template_name, {
            "buku":obj
        })
    

