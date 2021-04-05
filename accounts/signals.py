from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, PersonalTrainer, Client


@receiver(post_save, sender=CustomUser)
def create_personal_client(sender, instance, created, **kwargs):
	if created:
		if instance.is_pt:
			PersonalTrainer.objects.create(username=instance)

		elif instance.is_client:
			Client.objects.create(username=instance)
