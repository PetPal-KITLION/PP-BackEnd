from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import MemberSerializer
from django.shortcuts import render

# Create your views here.

class SignupView(APIView):
    def post(self, request):
        serializer = MemberSerializer(data = request.data)
        if serializer.is_valid():
            member = serializer.save()
            token, _ = Token.objects.get_or_create(user=member)
            return Response({'token':token.key})
        return Response(serializer.errors, status =  400)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user:
            token,_ = Token.objects.get_or_create(user=user)
            return Response({'token':token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)