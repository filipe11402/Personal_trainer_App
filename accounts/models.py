from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	is_pt = models.BooleanField(default=False)
	is_client = models.BooleanField(default=False)


class PersonalTrainer(models.Model):
	username = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	is_pt = models.BooleanField(default=True)
	is_client = models.BooleanField(default=False)


	def __str__(self):
		return str(self.username)


class Client(models.Model):
	username = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	is_client = models.BooleanField(default=True)
	is_pt = models.BooleanField(default=False)
	personal = models.ForeignKey(PersonalTrainer, on_delete=models.CASCADE, blank=True, null=True)


	def __str__(self):
		return str(self.username)
