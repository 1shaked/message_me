from rest_framework import serializers
from .models import ChatConversion 
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        password = serializers.CharField(
            min_length=4,
            write_only=True,
            required=True,
            style={'input_type': 'password'}
        )

        fields = ['email', 'username', 'password',]
    def create(self, validated_data):
        print('create user')
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChatConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatConversion
        exclude = ['is_read']
    


class ChatConversionUpdate(serializers.ModelSerializer):
    class Meta:
        model = ChatConversion
        fields = ['subject' ,'message']
