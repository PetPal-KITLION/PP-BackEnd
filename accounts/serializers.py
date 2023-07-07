from rest_framework import serializers
from .models import Member, Review, Pet

class MemberBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        field = '__all__'
    
class MemberSignUpSerializer(MemberBaseSerializer):

    class Meta(MemberBaseSerializer.Meta):
        fields = ['id', 'name', 'email', 'nickname', 'password', 'phone']

class PetBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
        
        
class PetProfileSerializer(PetBaseSerializer):
    
    class Meta(PetBaseSerializer.Meta):
        fields=['name','species','age','feature']
        depth=1

    
class ReviewBaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
    