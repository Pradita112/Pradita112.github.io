from datetime import date
from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Album(models.Model):
    nama = models.CharField(max_length= 45)
    artist = models.CharField(max_length= 45)
    tanggal_rilis = models.DateField()
    gambar = models.ImageField(upload_to = 'album')

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'album'

class Buku(models.Model):
    judul = models.CharField(max_length= 45)
    pengarang = models.CharField(max_length= 45)
    tanggal_rilis = models.DateField()
    gambar = models.ImageField(upload_to = 'buku')

    def __str__(self) -> str:
        return self.judul

    class Meta:
        db_table = 'judul'






