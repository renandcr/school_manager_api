from rest_framework_simplejwt.authentication import JWTAuthentication 
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import permissions, status, response, views
from addresses.serializer import AddressSerializer 
from addresses.models import Address
from django.core import exceptions

class AddressCreateView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, student_id):
        try:
            serializer = AddressSerializer(data={**request.data, 'student': student_id})
            if not serializer.is_valid():
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)


class AddressView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, _, address_id):
        try:
            address = get_object_or_404(Address, id=address_id)
            serializer = AddressSerializer(address)
            return response.Response(serializer.data)

        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, address_id):
        try:
            address = get_object_or_404(Address, id=address_id)
            serializer = AddressSerializer(address, data=request.data, partial=True)
            if not serializer.is_valid():
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return response.Response(serializer.data)
        
        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, _, address_id):
        try:
            address = get_object_or_404(Address, id=address_id)
            address.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)

        except exceptions.ValidationError as error:
            return response.Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)

