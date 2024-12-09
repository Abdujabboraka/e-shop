from django import forms
from .models import Announcement, Comment, Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'category', 'image', 'price', 'address', 'telegram_id', 'phone']
        labels = {
            'title': '📌 Nomi',
            'content': '📝 E\'lon haqida',
            'category': '📂 Kategoriya',
            'image': '📸 Rasm',
            'price': '💰 Narx',
            'address': '🏠 Manzil',
            'phone': '📱 Telefon raqam',
            'telegram_id': '🗨️ Telegram id',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nomini kiriting'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ' tafsilotlarini kiriting...'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*', 'placeholder': 'Rasmni yuklash'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Narxni  (so\'m)'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon: +998901234567'}),
            'telegram_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Telegram id ('ohn_doe')"}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Fikr va Taklif',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2}),
        }


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
        labels = {
            'username': 'Foydalanuvchi nomi',
            'first_name': 'Ismi',
            'last_name': 'Familiya',
            'email': 'Email',
            'password1': 'Parol',
            'password2': 'Parolni qayta kitish',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username:'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismi:'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiya:'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parolni qayta kitish'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            if self.instance and self.instance.username == username:
                return username  # The username hasn't changed
            raise forms.ValidationError("This username is already taken.")
        return username



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'telegram_id', 'photo']
        labels = {
            'address': 'Manzil',
            'phone': 'Telefon raqam',
            'telegram_id': 'Telegram id',
            'photo': 'Rasm',
        }
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manzil'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam'}),
            'telegram_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': " '@' ni Yozmang! '@user' ❌   'user' ✅ "}),
            'photo': forms.FileInput(attrs={'class': 'form-control'})
        }

        help_texts = {
            'photo': 'JPG, PNG, GIF formatlarda rasmlar qo\'shilish mumkin. Rasmning rangi 1MB dan ko\'p emas.'
        }


