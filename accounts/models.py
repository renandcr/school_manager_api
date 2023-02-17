from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=75, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    school = models.ForeignKey('schools.school', on_delete=models.CASCADE, related_name='users', null=True)

    def __repr__(self):
        return f'[{self.id}] - {self.password}'