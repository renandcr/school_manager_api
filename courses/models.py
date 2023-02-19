from django.db import models
import uuid

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    students = models.ManyToManyField('students.student', blank=True, related_name='courses')
    school = models.ForeignKey('schools.school', on_delete=models.CASCADE, related_name='courses')

    def __repr__(self):
        return f'[{self.id} - {self.name}]'
