from django.db import models
import uuid

class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    branch = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75, unique=True)
    zip_code = models.CharField(max_length=8)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    phone = models.CharField(max_length=14)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __repr__(self):
        return f'[{self.id}] - {self.email}'
    

  

