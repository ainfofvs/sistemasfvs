# Generated by Django 2.1.4 on 2019-01-28 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0032_entidaderesponsavel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conselho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('con_sigla', models.CharField(max_length=100, verbose_name='Sigla')),
            ],
            options={
                'permissions': (('conselho_list', 'Pode listar conselho'), ('conselho_create', 'Pode cadastrar conselho'), ('conselho_update', 'Pode editar conselho'), ('conselho_view', 'Pode ver conselho'), ('conselho_delete', 'Pode deletar conselho')),
            },
        ),
        migrations.AddField(
            model_name='entidade',
            name='uf_conselho',
            field=models.CharField(blank=True, max_length=2, verbose_name='UF'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_cep',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_dt_inicio_func',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Data de Início do Funcionamento'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_endereco',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_numero',
            field=models.CharField(blank=True, default='', max_length=6, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='mun_nome',
            field=models.CharField(max_length=100, verbose_name='municipio'),
        ),
        migrations.AddField(
            model_name='entidade',
            name='conselho',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devisa.Conselho'),
        ),
    ]
