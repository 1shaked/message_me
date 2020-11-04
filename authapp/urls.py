from django.urls import path, include, re_path
from authapp.views import CreateUserView , ChatConversionView , ChatMessage, ChatMessageUpdate

urlpatterns = [
    #path('auth/', include('djoser.urls')),
    #path('auth/', include('djoser.urls.authtoken')),
    #path('jwt/', include('djoser.urls')),
    #path('jwt/', include('djoser.urls.jwt')), # (r'^auth/', include('djoser.urls.jwt'))
    path('user/', CreateUserView.as_view(), name='user'),
    path('chatConversion/', ChatConversionView.as_view(), name='chatConversion'),
    re_path(r'^chatMessage/(?P<pk>\d+)/(?P<user_id>\d+)', ChatMessage.as_view(), name='chatMessage'),
    re_path(r'^chatMessageUpdate/(?P<pk>\d+)/(?P<user_id>\d+)', ChatMessageUpdate.as_view(), name='chatMessageUpdate'),

]