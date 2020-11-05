from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from django.contrib.auth import get_user_model

from .serializers import UserSerializer, ChatConversionSerializer, ChatConversionUpdate
from .models import ChatConversion

# this class base views will create a user on post
class CreateUserView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# create a message or get all chat conversion for a user
class ChatConversionView(generics.ListCreateAPIView):
    queryset = ChatConversion.objects.all()
    serializer_class = ChatConversionSerializer
    permission_classes = [permissions.IsAuthenticated]# will be added to auth check at the end

    def get_queryset(self):
        sender  = self.request.query_params.get('sender', None)
        seen    = self.request.query_params.get('seen', None)
        print(self.request.query_params)
        if seen == 'read':
            chat_convertion = ChatConversion.objects.filter(sender = sender, is_read=True)
        elif seen == 'unread':
            chat_convertion = ChatConversion.objects.filter(sender = sender, is_read=False)
        else:
            chat_convertion = ChatConversion.objects.filter(sender = sender)
        chat_convertion.update(is_read=True) # after every request the is read will change to true
        return chat_convertion


# delete and get spesic message for user (sender or recevier)
class ChatMessage(generics.RetrieveDestroyAPIView):
    queryset = ChatConversion.objects.all()
    serializer_class  = ChatConversionSerializer

    def delete(self, request, *args, **kwargs):
        msg_id  = kwargs['pk']
        user_id = kwargs['user_id']
        # filter by msg id and user_id == sender or recevier
        chat_msg = ChatConversion.objects.filter(Q(pk=msg_id) ,Q(sender = user_id) | Q(receiver = user_id)  )
        delete_status = chat_msg.delete()
        if delete_status[0]:
            return Response({'deleted' : 'deleted well done'} , status=status.HTTP_204_NO_CONTENT)
        return Response({'deleted' : 'no object to delete'},  status=status.HTTP_204_NO_CONTENT)


# update / edit a chat message contetnt 
class ChatMessageUpdate(generics.UpdateAPIView):
    queryset = ChatConversion.objects.all()
    serializer_class  = ChatConversionUpdate

    