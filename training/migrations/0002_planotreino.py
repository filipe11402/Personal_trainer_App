# Generated by Django 3.1.7 on 2021-04-05 20:38

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210405_1728'),
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanoTreino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', smart_selects.db_fields.ChainedForeignKey(chained_field='personal_trainer', chained_model_field='username', on_delete=django.db.models.deletion.CASCADE, to='accounts.client')),
                ('exercicio', models.ManyToManyField(to='training.Exercicio')),
                ('personal_trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.personaltrainer')),
            ],
        ),
    ]
