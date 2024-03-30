from django.db import models
from base.models import BaseModel



class Author(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    nationaly = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    

class Book(BaseModel):
    id = models.AutoField(primary_key=True)
    titel = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    genre = models.CharField(max_length=150)
    published_Date = models.DateField(null=True)

    def __str__(self) -> str:
        return self.titel


