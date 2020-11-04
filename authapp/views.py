from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import authentication, permissions

from django.contrib.auth import get_user_model

from .serializers import UserSerializer, ChatConversionSerializer
from .models import ChatConversion

# this class base views will create a user on post
class CreateUserView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class ChatConversionView(generics.ListCreateAPIView):
    queryset = ChatConversion.objects.all()
    serializer_class = ChatConversionSerializer
    # permission_classes = [permissions.IsAuthenticated] will be added to auth check at the end

    def get_queryset(self):
        sender = self.request.query_params.get('sender', None)
        print(self.request.query_params)
        print(self.request.query_params)
        return ChatConversion.objects.filter(sender = sender)

