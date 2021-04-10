from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, PersonalTrainer, Client


@receiver(post_save, sender=CustomUser)
def create_personal_client(sender, instance, created, **kwargs):
	if created:
		if instance.is_pt:
			print("i entered the signal")
			PersonalTrainer.objects.create(username=instance)
		else:
			Client.objects.create(username=instance)
