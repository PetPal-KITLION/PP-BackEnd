import random
import string
from .models import Member
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from .serializers import MemberSerializer



# Create your views here.



# 회원가입
class SignupView(APIView):
    def post(self, request):
        serializer = MemberSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'회원가입 완료'})
        return Response(serializer.errors, status =  400)

# 로그인
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            member = Member.objects.get(email=email)
            token, _ = Token.objects.get_or_create(user=user)
            print(token)
            member.token = token.key
            member.save()
            return Response({'token':token.key})
        else:
            return Response({'message': '유저가 존재하지 않음'}, status=400)

# 로그아웃
class LogoutView(APIView):
    def get(self, request):
        token = request.headers.get('Authorization')
        if token:
            try:
                member = Member.objects.get(token=token)
                member.token = ''
                member.save()
                return Response({'message' : '로그아웃 완료'})
            except Token.DoesNotExist:
                return Response({'error':'토큰이 존재하지 않습니다'},status = 401)
        return Response({'error':'유효하지 않은 토큰이거나 토큰이 없습니다.'}, status=400)
    
# 이메일 인증 메일 보내기
class SendMailView(APIView):
    def post(self,request):
        useremail = request.data.get('email')
        random_code = generate_random_code()
        SendMail(random_code, useremail,'signup-verify')
        return Response({'code':random_code},status = 200)
    


# 이메일 / 닉네임 중복확인
class CheckDuplicateView(APIView):
    def post(self, request):
    
        nickname = request.data.get('nickname')
        email = request.data.get('email')
        
        if nickname and Member.objects.filter(nickname=nickname).exists(): # 중복 되는지 검사
            return Response({'message' : 'true'}, status = 400)
        if email and Member.objects.filter(email=email).exists(): # 중복 되는지 검사
            return Response({'message' : 'true'},status = 400)
        
        return Response({'response':'false'})
    
# 이메일 찾기
class FindEmailView(APIView):
    def post(self, request):

        name = request.data.get('name')
        phone = request.data.get('phone')
        User = get_user_model()
        
        try:
            user = User.objects.filter(name=name, phone=phone).first()
            user_email = user.email
            return Response({'email': user_email}, status=200)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
        
# 비밀번호 초기화 - 메일 인증
class ResetPasswordEmailView(APIView):
    def post(self, request):
        useremail = request.data.get('email')
        user = Member.objects.get(email=useremail)
        if user:
            random_code = generate_random_code()
            SendMail(random_code, useremail,'reset-verify')
            return Response({'code':random_code},status = 200)
        else:
            return Response({'error':'User not found'},status=404)

# 비밀번호 초기화 하기
class ResetPasswordSaveView(APIView):
    def post(self, request):

        useremail = request.data.get('email')
        reset_password = request.data.get('reset')

        user = Member.objects.get(email=useremail)

        if user:
            user.password = reset_password
            user.save()
            return Response({'message':'success'},status=200)

        return Response({'error':'실패'},status=400)


def SendMail(random_code, useremail, usage):
    if usage == 'reset-verify':
        title = 'PetPal 에서 보내는 비밀번호 재설정 메일 입니다.'
    elif usage == 'signup-verify':
        title = 'PetPal 에서 보내는 회원가입 인증 메일 입니다.'
    email = EmailMessage(
        title,
        random_code,
        to=[useremail])
    email.send()

def generate_random_code():
    length = 6
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return code