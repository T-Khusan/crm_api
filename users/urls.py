from django.urls import path, include

from users.views import RegisterApiView


urlpatterns = [
    #path('register/', include('dj_rest_auth.registration.urls'), name='register'),
    path('register/', RegisterApiView.as_view(), name='register'),
]
