from rest_framework import serializers
from courses.models import Course

class CouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'