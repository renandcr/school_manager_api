from django.db import models
import uuid

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    zip_code = models.CharField(max_length=8)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    student = models.OneToOneField('students.student', on_delete=models.CASCADE)

    def __repr__(self):
        return f'[{self.id}] - {self.street}'
