from rest_framework import serializers

from books.models import Book,Author
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' , 'password']
    
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

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


