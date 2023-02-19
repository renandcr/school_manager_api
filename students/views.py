from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import views, response, permissions, status
from students.serializer import StudentSerializer
from students.models import Student
from django.core import exceptions

class StudentView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, _, student_id):
        try:
            student = get_object_or_404(Student, id=student_id)
            serializer = StudentSerializer(student)
            return response.Response(serializer.data)

        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST) 
        
    def patch(self, request, student_id):
        try:
            student = get_object_or_404(Student, id=student_id)
            serializer = StudentSerializer(student, request.data, partial=True)
            if not serializer.is_valid():
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return response.Response(serializer.data)
        
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _, student_id):
        try:
            student = get_object_or_404(Student, id=student_id)
            student.delete()      
            return response.Response(status=status.HTTP_204_NO_CONTENT)      
        
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        

class StudentCreateGetView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, school_id):
        try:
            serializer = StudentSerializer(data={**request.data, 'gender': request.data['gender'].lower(),'school': school_id})
            if not serializer.is_valid():
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, _, school_id):
        try:
            students = get_list_or_404(Student, school=school_id)
            serializer = StudentSerializer(students, many=True)
            return response.Response(serializer.data)
        
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
    