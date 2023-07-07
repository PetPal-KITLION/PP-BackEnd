from rest_framework import serializers
from django.contrib.auth import get_user_model  
from .models import petsitters_post, petsitters_comment,petsitters_apply

User = get_user_model()

class PetsittersCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = petsitters_comment
        #fields = ['id','post_id']
        fields = '__all__'

class PetsittersPostBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = petsitters_post
        fields = '__all__'

class PetsittersPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = petsitters_post
        fields = '__all__' 

class PetsittersApplyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = petsitters_apply
        fields = '__all__'

class PetsittersApplyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = petsitters_apply
        fields = '__all__'