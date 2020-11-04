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
        sender  = self.request.query_params.get('sender', None)
        seen = self.request.query_params.get('seen', None)
        print(self.request.query_params)
        print()
        if seen == 'read':
            chat_convertion = ChatConversion.objects.filter(sender = sender, is_read=True)
        elif seen == 'unread':
            chat_convertion = ChatConversion.objects.filter(sender = sender, is_read=False)
        else:
            chat_convertion = ChatConversion.objects.filter(sender = sender)
        chat_convertion.update(is_read=True) # after every request the is read will change to true
        return chat_convertion

