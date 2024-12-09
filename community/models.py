from django.db import models
from home.models import User

# Create your models here.

class Opinion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='opinion')
    opinion = models.CharField(max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s opinion"

    class Meta:
        ordering = ['-created_at']

#Support model
class Support(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supports')
    subject = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to='support/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s support request"