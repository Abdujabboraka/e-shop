from django import forms
from django.contrib.auth.models import User
from .models import UserMessage

class MessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['content',]
        labels = {
            'content': 'Xabar'
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Xabar'})
        }
