from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from helpers.texting import *

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class TestTexting(APIView):

    def get(self, request):
        message = sendTextMessage('', 'Test message to test number')
        content = {'sid' : message.sid }
        return Response(content)
