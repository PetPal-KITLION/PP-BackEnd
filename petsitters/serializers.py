from rest_framework import serializers
from django.contrib.auth import get_user_model  
from .models import petsitters_post, petsitters_comment

User = get_user_model()

class PetsittersCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = petsitters_comment
        fields = '__all__'

class PetsittersPostBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = petsitters_post
        fields = '__all__'

class PetsittersPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = petsitters_post
        fields = ['id', 'title', 'content', 'created_at'] 

    class Meta:
        model = petsitters_post
        fields = '__all__'
