# Generated by Django 2.1.4 on 2019-01-10 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0006_auto_20190108_0834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entidade',
            options={'permissions': (('entidade_list', 'Pode listar entidade'), ('entidade_create', 'Pode cadastrar entidade'), ('entidade_update', 'Pode editar entidade'), ('entidade_view', 'Pode ver entidade'), ('entidade_delete', 'Pode deletar entidade'), ('cnpj_validacao', 'Pode validar CNPJ'), ('cnpj', 'Pode informar CNPJ para validação'), ('cnpj_update', 'Pode editar CNPJ'), ('cnpj_view', 'Pode ver CNPJ'), ('cnpj_delete', 'Pode deletar CNPJ'))},
        ),
        migrations.AlterField(
            model_name='entidade',
            name='bairro',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='devisa.Bairro'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_cep',
            field=models.CharField(blank=True, max_length=10, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_cnes',
            field=models.CharField(blank=True, max_length=100, verbose_name='CNES (Estabelecimentos de Saúde)'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_cnpj',
            field=models.CharField(blank=True, default='', max_length=20, unique=True, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_complemento',
            field=models.CharField(blank=True, max_length=300, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_cpf',
            field=models.CharField(blank=True, default='', max_length=20, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_dt_expedicao',
            field=models.CharField(blank=True, max_length=10, verbose_name='Data de Expedição'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_dt_inicio_func',
            field=models.CharField(blank=True, max_length=10, verbose_name='Data de Início do Funcionamento'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_email',
            field=models.CharField(blank=True, max_length=200, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_endereco',
            field=models.CharField(blank=True, max_length=300, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_especializacao',
            field=models.CharField(blank=True, max_length=200, verbose_name='Especialização'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_fantasia',
            field=models.CharField(blank=True, max_length=200, verbose_name='nome Fantasia'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_fax',
            field=models.CharField(blank=True, max_length=15, verbose_name='Fax'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_fone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_insc_estadual',
            field=models.CharField(blank=True, max_length=100, verbose_name='Inscrição Estadual'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_insc_municipal',
            field=models.CharField(blank=True, max_length=100, verbose_name='Inscrição Municipal'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_nome_razao',
            field=models.CharField(blank=True, max_length=300, verbose_name='nome / Razão Social'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_obj_contrato_social',
            field=models.CharField(blank=True, max_length=500, verbose_name='Objetivo Contrato Social'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_observacoes',
            field=models.CharField(blank=True, max_length=500, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_orgao_exp',
            field=models.CharField(blank=True, max_length=100, verbose_name='Órgão Expedidor'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_pasta_num',
            field=models.CharField(blank=True, max_length=200, verbose_name='Número da Pasta'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_registro_conselho',
            field=models.CharField(blank=True, max_length=100, verbose_name='Registro no Conselho'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_rg',
            field=models.CharField(blank=True, max_length=20, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_tipo_entidade',
            field=models.CharField(choices=[(1, 'Pessoa Jurídica'), (2, 'Autônomo'), (3, 'Profissional Liberal'), (4, 'Responsável Técnico'), (5, 'Responsável Legal')], max_length=1, verbose_name='tipo de entidade'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='municipio',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='devisa.Municipio'),
        ),
    ]
