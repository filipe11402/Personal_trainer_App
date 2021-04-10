from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):

	is_pt = forms.BooleanField(required=False)

	class Meta:
		model = CustomUser
		fields = ['username', 'password1', 'password2', 'is_pt']
