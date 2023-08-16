from rest_framework.response import Response
from  rest_framework.decorators import api_view
from api import serializers

## Importaciones

from .models import Book
from .serializers import BookSerializer

'''
Obtiene todos los registros existentes
'''
@api_view(['GET'])
def getBook(request):
    #trae todo los datos de la BDD
    book = Book.objects.all()
    serializers = BookSerializer(book, many=True)
    return Response(serializers.data)

'''
Inserta un registro en la BDD
'''
@api_view(['POST'])
def postBook(request):
    data = request.data
    book = Book.objects.create(
        ISBN = data['ISBN'],
        book_title = data['book_title'],
        book_author = data['book_author'],
        year_of_publication = data['year_of_publication'],
        publisher =  data['publisher'],
        image_URL_S =  data['image_URL_S'],
        image_URL_M = data['image_URL_M'],
        image_URL_L = data['image_URL_L'],

    )
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

'''
Actualiza un registro dado el id del mismo
'''
@api_view(['PUT'])
def putBook(request, pk):
    data = request.data
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print(serializer.errors)
        return Response('Hubo un peo!')
        

'''
Elimina un registro dado el id del mismo
'''
@api_view(['DELETE'])
def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return Response('Book deleted!')
