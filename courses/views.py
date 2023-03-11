from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import response, permissions, status, views
from courses.serializer import CourseSerializer
from students.models import Student
from django.core import exceptions
from courses.models import Course
from accounts.models import User

class CourseCreateGetView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, school_id):
        try: 
            serializer = CourseSerializer(data={**request.data, 'school': school_id})
            if not serializer.is_valid():
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, _, school_id): 
        try:
            courses = get_list_or_404(Course, school=school_id)
            serializer = CourseSerializer(courses, many=True)
            return response.Response(serializer.data)

        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)


class CourseView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, _, course_id):
        try:
            course = get_object_or_404(Course, id=course_id)
            serializer = CourseSerializer(course)
            return response.Response(serializer.data)

        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, course_id): 
        try:
            course = get_object_or_404(Course, id=course_id)
            serializer = CourseSerializer(course, request.data, partial=True)
            if not serializer.is_valid():
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return response.Response(serializer.data)

        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, _, course_id):
        try:
            course = get_object_or_404(Course, id=course_id)
            course.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)

        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)


class CourseAddAndRemoveStudentView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, _, course_id, student_email):
        try:
            course = get_object_or_404(Course, id=course_id)
            student = get_object_or_404(Student, email=student_email)
            course.students.add(student)
            serializer = CourseSerializer(course)
            return response.Response(serializer.data)
        
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, _, course_id, student_email):
        try:
            course = get_object_or_404(Course, id=course_id)
            student = get_object_or_404(Student, email=student_email)
            course.students.remove(student)
            serializer = CourseSerializer(course)
            return response.Response(serializer.data)

        except exceptions.ValidationError as error: 
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)


class CourseAddAndRemoveInstructorView(views.APIView):
    def post(self, _, course_id, user_email):
        try:
            course = get_object_or_404(Course, id=course_id)
            user = get_object_or_404(User, email=user_email)
            if (user.role == "instrutor(a) de ensino"):
                course.instructors.add(user)
                serializer = CourseSerializer(course)
                return response.Response(serializer.data)
            else:
                return response.Response({"error": "O cargo deste funcionário não é de instrutor"}, status=status.HTTP_400_BAD_REQUEST)
            
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, _, course_id, user_email):
        try: 
            course = get_object_or_404(Course, id=course_id)
            user = get_object_or_404(User, email=user_email)
            course.instructors.remove(user)
            serializer = CourseSerializer(course)
            return response.Response(serializer.data)
        
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        