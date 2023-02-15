from rest_framework import views, response, status
from schools.serializer import SchoolSerializer
from django.core import exceptions
from schools.models import School

class SchoolView(views.APIView):
    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if(not serializer.is_valid()):
            return response.Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request): 
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return response.Response(serializer.data)

    def patch(self, request, school_id): 
        try:
            school = School.objects.get(id=school_id)
            serializer = SchoolSerializer(school, request.data, partial=True)
            if(not serializer.is_valid()):
                return response.Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return response.Response(serializer.data)

        except TypeError as error:
           return response.Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)
        except exceptions.ObjectDoesNotExist as error:
            return response.Response({"error": [f"No results for {school_id}"]}, status=status.HTTP_404_NOT_FOUND)
        except exceptions.ValidationError as error:
            return response.Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, school_id):
        try:
            school = School.objects.get(id=school_id)
            school.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)

        except exceptions.ObjectDoesNotExist as error:
            return response.Response({"error": [f"No results for {school_id}"]}, status=status.HTTP_404_NOT_FOUND)
        except exceptions.ValidationError as error:
            return response.Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)
