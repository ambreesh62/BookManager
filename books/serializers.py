from rest_framework import serializers

from books.models import Book,Author


class AutorSerializers(serializers.ModelSerializer):

    class Meta:
        model = Author
        # fields = ['id','name','date_of_birth', 'nationaly']
        exclude =[]

class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model = Book
        # fields = ['titel','id']
        # field = '__all__'

        exclude =[]


