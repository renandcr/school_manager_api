from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import views, response, status, permissions
from accounts.serializer import UserSerializer
from django.core import exceptions
from schools.models import School
from accounts.models import User

class UserCreateView(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()    
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
class UserAddSchoolView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def patch(self, _, school_id, user_email):
        try:
            user = get_object_or_404(User, email=user_email)
            school = get_object_or_404(School, id=school_id)
            user.school = school
            serializer_update = UserSerializer(user, user.__dict__, partial=True)
            if not serializer_update.is_valid():
                return response.Response(serializer_update.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer_update.save()    
                return response.Response(serializer_update.data)
        
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)


class UserGetView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, _, school_id):
        try:
            users = get_list_or_404(User, school=school_id)
            serializer = UserSerializer(users, many=True)
            return response.Response(serializer.data)
        
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)


class UserView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def patch(self, request, user_id):
        try:
            user = get_object_or_404(User, id=user_id)
            serializer = UserSerializer(user, request.data, partial=True)
            if not serializer.is_valid():
                return response.Response(serializer.errors)
            else: 
                serializer.save()
                return response.Response(serializer.data)
            
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, _, user_id):
        try:
            user = get_object_or_404(User, id=user_id)
            user.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)

            