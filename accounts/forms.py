from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):

	BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

	is_pt = forms.TypedChoiceField(coerce=lambda x: x=='True', choices=BOOL_CHOICES, widget=forms.RadioSelect)

	class Meta:
		model = CustomUser
		fields = ['username', 'password1', 'password2', 'is_pt']
