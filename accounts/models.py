from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class Role(models.TextChoices):
    DIRECTOR = ('diretor(a)')
    PSYCHOLOGIST = ('psicólogo(a)')
    TEACHING_INSTRUCTOR = ('instrutor(a) de ensino')
    TEACHING_MONITOR = ('monitor(a) de ensino')
    SECRETARY = ('secretário(a)')
    OTHER = ('outros')


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=75, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.OTHER)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'role']

    school = models.ForeignKey('schools.school', on_delete=models.CASCADE, related_name='users', null=True)

    def __repr__(self):
        return f'[{self.id}] - {self.password}'