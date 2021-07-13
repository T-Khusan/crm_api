from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegistrationSerializer


class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
