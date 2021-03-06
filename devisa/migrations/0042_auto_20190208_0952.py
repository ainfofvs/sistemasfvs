# Generated by Django 2.1.4 on 2019-02-08 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0041_auto_20190131_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Areaproducao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ap_nome', models.CharField(default='', max_length=200, verbose_name='nome')),
                ('ap_descricao', models.CharField(default='', max_length=400, verbose_name='descrição')),
            ],
            options={
                'permissions': (('area_producao_list', 'Pode listar área de produção'), ('area_producao_create', 'Pode cadastrar área de produção'), ('area_producao_update', 'Pode editar área de produção'), ('area_producao_view', 'Pode ver área de produção'), ('area_producao_delete', 'Pode deletar área de produção')),
            },
        ),
        migrations.CreateModel(
            name='Classeproducao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp_nome', models.CharField(default='', max_length=200, verbose_name='nome')),
                ('cp_descricao', models.CharField(default='', max_length=400, verbose_name='descrição')),
                ('area_producao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devisa.Areaproducao')),
            ],
            options={
                'permissions': (('classe_producao_list', 'Pode listar classe de produção'), ('classe_producao_create', 'Pode cadastrar classe de produção'), ('classe_producao_update', 'Pode editar classe de produção'), ('classe_producao_view', 'Pode ver classe de produção'), ('classe_producao_delete', 'Pode deletar classe de produção')),
            },
        ),
        migrations.CreateModel(
            name='Formaproducao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fp_nome', models.CharField(default='', max_length=200, verbose_name='nome')),
                ('fp_descricao', models.CharField(default='', max_length=400, verbose_name='descrição')),
            ],
            options={
                'permissions': (('forma_producao_list', 'Pode listar forma de produção'), ('forma_producao_create', 'Pode cadastrar forma de produção'), ('forma_producao_update', 'Pode editar forma de produção'), ('forma_producao_view', 'Pode ver forma de produção'), ('forma_producao_delete', 'Pode deletar forma de produção')),
            },
        ),
        migrations.CreateModel(
            name='Linhaproducao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lp_nome', models.CharField(default='', max_length=200, verbose_name='nome')),
                ('lp_descricao', models.CharField(default='', max_length=400, verbose_name='descrição')),
                ('area_producao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devisa.Areaproducao')),
            ],
            options={
                'permissions': (('linha_producao_list', 'Pode listar linha de produção'), ('linha_producao_create', 'Pode cadastrar linha de produção'), ('linha_producao_update', 'Pode editar linha de produção'), ('linha_producao_view', 'Pode ver linha de produção'), ('linha_producao_delete', 'Pode deletar linha de produção')),
            },
        ),
        migrations.AddField(
            model_name='formaproducao',
            name='linha_producao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devisa.Linhaproducao'),
        ),
    ]
