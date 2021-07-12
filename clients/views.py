from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from clients.models import Client
from clients.serializers import ClientSerializer


class ClientListApiView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)