from django.db import models
from accounts.models import PersonalTrainer, Client
from smart_selects.db_fields import ChainedForeignKey


class Exercicio(models.Model):
    nome = models.CharField(max_length=50)
    series = models.IntegerField(blank=False)
    repeticoes = models.IntegerField(blank=False)


    def __str__(self):
        return self.nome


class PlanoTreino(models.Model):
    personal_trainer = models.ForeignKey(PersonalTrainer, on_delete=models.CASCADE)
    client = ChainedForeignKey(
        Client,
        chained_field='personal_trainer',
        chained_model_field='personal',
        show_all=False,
    )
    exercicio = models.ManyToManyField(Exercicio)


    def __str__(self):
        return str(self.personal_trainer)
