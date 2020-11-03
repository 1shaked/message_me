from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser

# Create the user model.
class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    username = models.CharField(max_length=255)
    REQUIRED_FIELDS = ['username', 'phone'] 
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
    
    def __str__(self):
        return self.email


class ChatConversion(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='sender',
        on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='receiver',
        on_delete=models.CASCADE)

    subject = models.CharField(max_length=150)
    message = models.TextField(null=True)
    date = models.DateField(auto_now_add=True, null=True)
    is_read = models.BooleanField(default=False)
    def __str__(self):
        msg_status = 'unread'
        if this.is_read:
            msg_status = 'read'
        return f'''
            the sender {this.sender} 
            send to {this.receiver} 
            msg with the subject {this.subject}
            at {this.date}
            The msg status is {msg_status}
            '''