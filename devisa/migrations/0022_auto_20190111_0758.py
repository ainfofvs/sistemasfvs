# Generated by Django 2.1.4 on 2019-01-11 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0021_auto_20190110_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entidade',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_cep',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_cnes',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_complemento',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_dt_expedicao',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_dt_inicio_func',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_email',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_endereco',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_especializacao',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_fantasia',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_fax',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_fone',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_insc_estadual',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_insc_municipal',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_numero',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_obj_contrato_social',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_observacoes',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_orgao_exp',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_pasta_num',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_registro_conselho',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='ent_rg',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='escolaridade',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='formacao_profissional',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='entidade',
            name='natureza_juridica_dependencia',
        ),
    ]
