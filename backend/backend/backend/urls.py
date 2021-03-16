from django.urls import path

from main import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
