from django.db import models
import uuid

class Gender(models.TextChoices):
    MASCULINE = ('masculino')
    FEMININE = ('feminino')
    OTHER = ('outro')


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75, unique=True)
    date_of_birth = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=14)
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.OTHER)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    school = models.ForeignKey('schools.school', on_delete=models.CASCADE, related_name='students')
