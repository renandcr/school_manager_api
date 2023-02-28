from students.serializer import StudentSerializer
from rest_framework import serializers
from courses.models import Course

class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = '__all__'