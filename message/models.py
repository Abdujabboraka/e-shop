from django.contrib.auth.models import User
from django.db import models


class UserMessage(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_messages', verbose_name='avtor')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', verbose_name='jonatuvchi')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', verbose_name='qabulqiluvchi')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"