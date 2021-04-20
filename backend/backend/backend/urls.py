from django.urls import path

from main import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    ## Testing
    path('api/tests/texting', views.TestTexting.as_view(), name='test-texting'),
]
