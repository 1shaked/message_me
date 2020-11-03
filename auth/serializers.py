from rest_framework import serializers
from auth.models import ChatConversion 

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = settings.AUTH_USER_MODEL
        fields = '__all__'


class ChatConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatConversion
        exclude = ['date', 'is_read']
    
