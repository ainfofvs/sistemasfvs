# Generated by Django 2.1.4 on 2019-01-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0029_auto_20190115_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entidadesubatividade',
            name='entidade',
        ),
        migrations.RemoveField(
            model_name='entidadesubatividade',
            name='subatividade',
        ),
        migrations.AddField(
            model_name='subatividade',
            name='entidades',
            field=models.ManyToManyField(to='devisa.Entidade'),
        ),
        migrations.DeleteModel(
            name='EntidadeSubatividade',
        ),
    ]
