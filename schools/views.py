from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import views, response, status, permissions
from schools.serializer import SchoolSerializer
from django.shortcuts import get_object_or_404
from django.core import exceptions
from schools.models import School

class SchoolView(views.APIView):
    uthentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if not serializer.is_valid():
            return response.Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, _): 
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return response.Response(serializer.data)

    def patch(self, request, school_id): 
        try:
            school = get_object_or_404(School, id=school_id)
            serializer = SchoolSerializer(school, request.data, partial=True)
            if not serializer.is_valid():
                return response.Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return response.Response(serializer.data)

        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, _, school_id):
        try:
            school = get_object_or_404(School, id=school_id)
            school.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)

        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
