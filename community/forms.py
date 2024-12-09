from django import  forms
from django.contrib.auth.models import User
from .models import Opinion, Support
class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['opinion']
        labels = {
            'opinion': 'Fikr va Taklif'
        }
        widgets = {
            'opinion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fikr va Taklif ...'})
        }





class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['subject','content','photo']
        labels = {
            'subject': 'Mavzu',
            'content': 'Asosiy masala',
            'photo': 'Rasm'
        }
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mavzu ...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Asosiy masala ...'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'image/jpeg, image/png'}),
        }

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            if photo.content_type not in ['image/jpeg', 'image/png']:
                raise forms.ValidationError('Only JPEG and PNG images are allowed')
            if photo.size > 5242880:  # 5MB
                raise forms.ValidationError('Image size should not exceed 5MB')
        return photo
