from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
	model = CustomUser
	fields = ['username', 'password1', 'password2', 'is_pt', 'is_client']
