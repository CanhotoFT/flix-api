from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('authentication/token/', TokenObtainPairView, name='token_obtain_pair'),
]