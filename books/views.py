from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Author
from books.serializers import AutorSerializers,BookSerializers
from rest_framework import status

# AUTHOR CURD [GET,POST, PUT, PATCH. DEL]

@api_view(["GET"])
def get_author(request):
    author_objs = Author.objects.all()
    serializer = AutorSerializers(author_objs, many=True)
    return Response({"message": 200, "payload": serializer.data})


@api_view(['POST'])
def post_author(request):

    if request.method == 'POST':
        serializer = AutorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_author(request, id):

   try:
       author_obj = Author.objects.get(id=id)
       serializer = AutorSerializers(author_obj, data = request.data)

    
       if request.method == 'PUT':
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   except Exception as e:
       print(e)
       return Response({'status' : 403, 'massage': 'id not valid'})
     

@api_view(['PATCH'])
def patch_author(request, id):

   try:
       author_obj = Author.objects.get(id=id)
       serializer = AutorSerializers(author_obj, data = request.data, partial=True)

    
       if request.method == 'PATCH':
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   except Exception as e:
       print(e)
       return Response({'status' : 403, 'massage': 'id not valid'})
   

@api_view(['DELETE'])
def delete_author(request, id):
    try:
        
        author_obj = Author.objects.get(id = id)

        if request.method == 'DELETE':
          author_obj.delete()
          return Response({'status' : 200, 'massage' : 'deleted'})   
            
    except Exception as e:
        print(e)
        return Response({'status' : 403, 'massage': 'id not valid'})        
    


# BOOK CRUD [GET, POST, PUT, PATCH, DEL]
    
@api_view(["GET"])
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializers(book_objs, many=True)
    return Response({"message": 200, "payload": serializer.data})


@api_view(['POST'])
def post_book(request):

    if request.method == 'POST':
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_book(request, id):

   try:
       book_obj = Book.objects.get(id=id)
       serializer = BookSerializers(book_obj, data = request.data)

    
       if request.method == 'PUT':
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   except Exception as e:
       print(e)
       return Response({'status' : 403, 'massage': 'id not valid'})
   

@api_view(['PATCH'])
def patch_book(request, id):

   try:
       book_obj = Book.objects.get(id=id)
       serializer = BookSerializers(book_obj, data = request.data, partial=True)

    
       if request.method == 'PATCH':
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   except Exception as e:
       print(e)
       return Response({'status' : 403, 'massage': 'id not valid'})   
   

@api_view(['DELETE'])
def delete_book(request, id):
    try:
        
        Book_obj = Book.objects.get(id = id)

        if request.method == 'DELETE':
          Book_obj.delete()
          return Response({'status' : 200, 'massage' : 'deleted'})   
            
    except Exception as e:
        print(e)
        return Response({'status' : 403, 'massage': 'id not valid'})         
   
