# Generated by Django 2.1.4 on 2019-01-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0024_auto_20190111_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidade',
            name='ent_cnpj',
            field=models.CharField(max_length=30, unique=True, verbose_name='CNPJ'),
        ),
    ]
