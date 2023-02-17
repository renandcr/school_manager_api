from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import views, response, status, permissions
from accounts.serializer import UserSerializer
from django.core import exceptions
from schools.models import School
from accounts.models import User

class UserCreateView(views.APIView):
    def post(self, request, school_id):
        try:
            school = get_object_or_404(School, id=school_id)
            serializer = UserSerializer(data={**request.data, 'school': school.id})
            if not serializer.is_valid():
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()    
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)

class UserView(views.APIView):
    uthentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
        
    def get(self, _, school_id):
        try:
            users = get_list_or_404(User, school=school_id)
            serializer = UserSerializer(users, many=True)
            return response.Response(serializer.data)
        
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, school_id, user_id):
        try:
            user = get_object_or_404(User, id=user_id, school=school_id)
            serializer = UserSerializer(user, request.data, partial=True)
            if not serializer.is_valid():
                return response.Response(serializer.errors)
            else: 
                serializer.save()
                return response.Response(serializer.data)
            
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, _, school_id, user_id):
        try:
            user = get_object_or_404(User, id=user_id, school=school_id)
            user.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)