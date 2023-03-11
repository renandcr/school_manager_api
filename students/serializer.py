from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'

