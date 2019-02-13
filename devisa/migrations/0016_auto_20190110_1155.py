# Generated by Django 2.1.4 on 2019-01-10 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0015_auto_20190110_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidade',
            name='escolaridade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='devisa.Escolaridade'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='formacao_profissional',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='devisa.Formacao'),
        ),
    ]