# Generated by Django 2.1.4 on 2019-02-14 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0045_auto_20190214_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidade',
            name='bairro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devisa.Bairro'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='conselho',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devisa.Conselho'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='escolaridade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devisa.Escolaridade'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='formacao_profissional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devisa.Formacao'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devisa.Municipio'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='natureza_juridica_dependencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devisa.Natureza'),
        ),
    ]