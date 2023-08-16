from django.db import models

# Create your models here.

# Creacion del modelo para Libros
class Book(models.Model):
    ISBN = models.CharField(max_length=50, blank=True)
    book_title = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50 , blank=True)
    year_of_publication = models.CharField(max_length=50 , blank=True)
    publisher =  models.CharField(max_length=50 , blank=True)
    image_URL_S =  models.CharField(max_length=50 , blank=True)
    image_URL_M = models.CharField(max_length=50 , blank=True)
    image_URL_L = models.CharField(max_length=50 , blank=True)

    def __str__(self):
        return self.ISBN + ", " + self.book_title +  ", " + self.book_author + self.book_title + ", " + self.year_of_publication +  ", " + self.publisher + self.image_URL_S + ", " + self.image_URL_M +  ", " + self.image_URL_L