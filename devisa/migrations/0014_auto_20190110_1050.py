# Generated by Django 2.1.4 on 2019-01-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0013_entidade_ent_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidade',
            name='ent_numero',
            field=models.CharField(max_length=6, verbose_name='Endereço'),
        ),
    ]
