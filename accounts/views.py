import random
import string
from .models import Member, Review, Pet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.core.exceptions import ObjectDoesNotExist
from .serializers import MemberSignUpSerializer, PetProfileSerializer,PetBaseSerializer



# Create your views here.

class SignupView(APIView):
    def post(self, request):
        serializer = MemberSignUpSerializer(data = request.data)
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
            member.token = token.key
            member.save()
            return Response({'token':token.key,'nickname':member.nickname})
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
            except ObjectDoesNotExist:
                return Response({'error':'유효하지 않은 토큰입니다'},status = 400)
        return Response({'error':'로그인이 필요합니다'}, status=401)
    
# 이메일 인증 메일 보내기
class SendMailView(APIView):
    def post(self,request):
        useremail = request.data.get('email')
        random_code = generate_random_code()
        SendMail(random_code, useremail,'signup-verify')
        return Response({'code':random_code},status = 200)
    

# 회원 탈퇴

class DeleteMember(APIView):
    def post(self,request):
        
        token = request.headers.get('Authorization')
        if token:
            try:
                member = Member.objects.get(token=token)
                member.delete()
                return Response({'message':'탈퇴완료'}, status=200)
            except ObjectDoesNotExist:
                return Response({'error':'유효하지 않은 토큰입니다'},status = 400)
        return Response({'error':'로그인이 필요합니다'}, status=401)
    

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
    def put(self, request):

        useremail = request.data.get('email')
        reset_password = request.data.get('reset')

        user = Member.objects.get(email=useremail)

        if user:
            user.password = reset_password
            user.save()
            return Response({'message':'success'},status=200)

        return Response({'error':'실패'},status=400)
# 프로필 조회
class MyProfileView(APIView):
    
    def get(self,request):
        token = request.headers.get('Authorization')
        if token:
            try:
                member = Member.objects.get(token=token)
                serialized_pets= PetProfileSerializer(member.pets.all(), many=True).data
                reviews = member.received_reviews.all()
                total_scores = sum(review.score for review in reviews)
                
                if reviews.count() > 0:
                    average_score = total_scores/reviews.count()
                else:
                    average_score = 0
                
                profile_data = {
                    'name' : member.name,
                    'email' : member.email,
                    'nickname': member.nickname,
                    'phone' : member.phone,
                    'address' : member.address,
                    'age' : member.age,
                    'review_star' : average_score,
                    'pets' : serialized_pets,
                }
                
                return Response(profile_data, status=200)
            except ObjectDoesNotExist:
                return Response({'error':'유효하지 않은 토큰입니다'},status = 400)
        return Response({'error':'로그인이 필요합니다'}, status=401)

class EditProfileView(APIView):
    def put(self,request):
        token = request.headers.get('Authorization')
        if token:
            try:
                member = Member.objects.get(token=token)
                pet = Pet.objects.get(member=member)
                
                edit_address = request.data.get('address')
                edit_age = int(request.data.get('age'))
                edit_pet_name = request.data.get('pet_name')
                edit_pet_species = request.data.get('pet_species')
                edit_pet_age = int(request.data.get('pet_age'))
                edit_pet_feature = request.data.get('pet_feature')

               

                member.address = edit_address
                member.age = edit_age
                member.save()

                pet.name = edit_pet_name
                pet.species = edit_pet_species
                pet.age = edit_pet_age
                pet.feature = edit_pet_feature
                pet.save()


                return Response({'message':'수정완료'}, status=200)
            except ObjectDoesNotExist:
                return Response({'error':'유효하지 않은 토큰입니다'},status = 400)
        return Response({'error':'로그인이 필요합니다'}, status=401)
        
class RegistPetView(APIView):
    
    def post(self,request):
        useremail = request.data.get('email')
        pet_data = {
            'name' : request.data.get('pet_name'),
            'species' : request.data.get('pet_species'),
            'age' : int(request.data.get('pet_age')),
            'feature' : request.data.get('pet_feature')
        }
        try: 
            user = Member.objects.get(email=useremail)
        except Member.DoesNotExist:
            return Response({'error':'User not found'}, status=404)
        
        pet_data['member'] = user.id
        serializer = PetBaseSerializer(data=pet_data)
    
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'등록완료'},status=200)
        return Response({'error':'등록실패'},status=400)

class ReviewCreateView(APIView):
    def post(self,request):
        
        receiver_email = request.data.get('sitter_email')
        reviewer_email = request.data.get('host_email')
        content = request.data.get('content')
        star = request.data.get('star')
        
        try:
            User = get_user_model()
            receiver = User.objects.get(email=receiver_email)
            reviewer = User.objects.get(email=reviewer_email)
        except User.DoesNotExist:
            return Response({'error': '유효하지 않은 이메일 주소'}, status=400)
        
        Review.objects.create(content=content, score=star, reviewer=reviewer, receiver=receiver)
        return Response({'message': '리뷰가 성공적으로 작성되었습니다'}, status=201)

class ReviewListView(APIView):
    def get(self, request):
        
        token = request.headers.get('Authorization')

        if token:
            try:
                member = Member.objects.get(token=token)
                reviews = member.received_reviews.all()
                review_data={'review':[]}
                for review in reviews:
                    review_data['review'].append({
                        'review_id':review.id,
                        'email' : review.reviewer.email,
                        'star' : review.score,
                        'content'  : review.content
                    })
                return Response(review_data, status=200)
            except ObjectDoesNotExist:
                return Response({'error':'유효하지 않은 토큰입니다'},status = 400)
        return Response({'error':'로그인이 필요합니다'}, status=401)

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