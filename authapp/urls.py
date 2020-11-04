from django.urls import path, include, re_path
from authapp.views import CreateUserView , ChatConversionView

urlpatterns = [
    #path('auth/', include('djoser.urls')),
    #path('auth/', include('djoser.urls.authtoken')),
    #path('jwt/', include('djoser.urls')),
    #path('jwt/', include('djoser.urls.jwt')), # (r'^auth/', include('djoser.urls.jwt'))
    path('user/', CreateUserView.as_view(), name='user'),
    path('chatConversion/', ChatConversionView.as_view(), name='chatConversion'),
    #re_path(r'^chat-view/(?P<pk>\d+)/', ChatDetails.as_view(), name='chat-view'),
]