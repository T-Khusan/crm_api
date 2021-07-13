from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from clients.models import Client
from clients.serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


'''
class ClientListApiView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(instance=clients, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ClientDetailApiView(APIView):

    def get(self, request, id):
        try:
            client = Client.objects.get(pk=id)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(instance=client)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id):
        try:
            client = Client.objects.get(pk=id)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(instance=client, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id):
        try:
            client = Client.objects.get(pk=id)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(instance=client, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        try:
            client = Client.objects.get(pk=id)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        client.delete()

        return Response(data={'message':'deleted'}, status=status.HTTP_204_NO_CONTENT)
'''
