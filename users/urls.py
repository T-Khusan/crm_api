from django.urls import path, include

from users.views import RegisterApiView


urlpatterns = [
    #path('register/', include('dj_rest_auth.registration.urls'), name='register'),
    path('register/', RegisterApiView.as_view(), name='register'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]
