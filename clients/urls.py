'''
from django.urls import path

from clients.views import ClientListApiView, ClientDetailApiView


urlpatterns = [
    path('', ClientListApiView.as_view(), name='clients'),
    path('<int:id>/', ClientDetailApiView.as_view(), name='detail')
]
'''
from rest_framework import routers

from clients.views import ClientViewSet


router = routers.DefaultRouter()
router.register('', ClientViewSet, basename='client')


urlpatterns = router.urls
