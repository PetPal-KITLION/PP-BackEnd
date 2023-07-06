import random
import string
from .models import Member
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .serializers import MemberSerializer
from django.core.mail import EmailMessage



# Create your views here.

class SignupView(APIView):
    def post(self, request):
        serializer = MemberSerializer(data = request.data)
        if serializer.is_valid():
            member = serializer.save()
            token, _ = Token.objects.get_or_create(user=member)
            return Response({'token':token.key})
        return Response(serializer.errors, status =  400)

@permission_classes([AllowAny])    
class LoginView(APIView):
    def post(self, request):
        
        email = request.data.get('email')
        password = request.data.get('password')
        print(email,password)

        user = authenticate(request, email=email, password=password)
        
        print(user)
        if user:
            token = Token.objects.get(user=user)
            return Response({'token':token.key})
        else:
            
            return Response({'error': 'Invalid credentials'}, status=401)

class SendMailView(APIView):
    
    def generate_random_code(self):
        length = 6
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for _ in range(length))
        return code
    
    def post(self,request):
        
        useremail = request.data.get('email')
        random_code = self.generate_random_code()
        email = EmailMessage(
            'PetPal 에서 보내는 인증 메일 입니다.',
            random_code,
            to=[useremail]
        )
        email.send()
        return Response({'code':random_code},status = 200)
    
class CheckDuplicateView(APIView):
    def post(self, request):
        print(request)
        nickname = request.data.get('nickname')
        email = request.data.get('email')
        
        if nickname and Member.objects.filter(nickname=nickname).exists(): # 중복 되는지 검사
            return Response({'response' : 'true'}, status = 400)
        if email and Member.objects.filter(email=email).exists(): # 중복 되는지 검사
            return Response({'response' : 'true'},status = 400)
        
        return Response({'response':'false'})