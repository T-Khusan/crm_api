from django.urls import path

from clients.views import ClientListApiView


urlpatterns = [
    path('', ClientListApiView.as_view(), name='clients'),
]