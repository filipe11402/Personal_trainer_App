# Generated by Django 3.1.7 on 2021-04-05 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210405_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='personal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.personaltrainer'),
        ),
    ]
