from django.urls import path, include, re_path
from authapp.views import CreateUserView , ChatConversionView , ChatMessage, ChatMessageUpdate
from rest_framework.authtoken.views import obtain_auth_token  

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('user/', CreateUserView.as_view(), name='user'),
    path('chatConversion/', ChatConversionView.as_view(), name='chatConversion'),
    re_path(r'^chatMessage/(?P<pk>\d+)/(?P<user_id>\d+)', ChatMessage.as_view(), name='chatMessage'),
    re_path(r'^chatMessageUpdate/(?P<pk>\d+)/(?P<user_id>\d+)', ChatMessageUpdate.as_view(), name='chatMessageUpdate'),

]