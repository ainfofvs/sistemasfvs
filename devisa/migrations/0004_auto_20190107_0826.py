# Generated by Django 2.1.4 on 2019-01-07 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0003_auto_20190107_0752'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'permissions': (('area_list', 'Pode listar área'), ('area_create', 'Pode cadastrar área'), ('area_update', 'Pode editar área'), ('area_view', 'Pode ver área'), ('area_delete', 'Pode deletar área'))},
        ),
        migrations.AlterModelOptions(
            name='atividade',
            options={'permissions': (('atividade_list', 'Pode listar atividade'), ('atividade_create', 'Pode cadastrar atividade'), ('atividade_update', 'Pode editar atividade'), ('atividade_view', 'Pode ver atividade'), ('atividade_delete', 'Pode deletar atividade'))},
        ),
        migrations.AlterModelOptions(
            name='bairro',
            options={'permissions': (('bairro_list', 'Pode listar bairro'), ('bairro_create', 'Pode cadastrar bairro'), ('bairro_update', 'Pode editar bairro'), ('bairro_view', 'Pode ver bairro'), ('bairro_delete', 'Pode deletar bairro'))},
        ),
        migrations.AlterModelOptions(
            name='entidade',
            options={'permissions': (('entidade_list', 'Pode listar entidade'), ('entidade_create', 'Pode cadastrar entidade'), ('entidade_update', 'Pode editar entidade'), ('entidade_view', 'Pode ver entidade'), ('entidade_delete', 'Pode deletar entidade'))},
        ),
        migrations.AlterModelOptions(
            name='entidadeatividade',
            options={'permissions': (('entidadeatividade_list', 'Pode listar entidadeatividade'), ('entidadeatividade_create', 'Pode cadastrar entidadeatividade'), ('entidadeatividade_update', 'Pode editar entidadeatividade'), ('entidadeatividade_view', 'Pode ver entidadeatividade'), ('entidadeatividade_delete', 'Pode deletar entidadeatividade'))},
        ),
        migrations.AlterModelOptions(
            name='escolaridade',
            options={'permissions': (('escolaridade_list', 'Pode listar escolaridade'), ('escolaridade_create', 'Pode cadastrar escolaridade'), ('escolaridade_update', 'Pode editar escolaridade'), ('escolaridade_view', 'Pode ver escolaridade'), ('escolaridade_delete', 'Pode deletar escolaridade'))},
        ),
        migrations.AlterModelOptions(
            name='estado',
            options={'permissions': (('estado_list', 'Pode listar estado'), ('estado_create', 'Pode cadastrar estado'), ('estado_update', 'Pode editar estado'), ('estado_view', 'Pode ver estado'), ('estado_delete', 'Pode deletar estado'))},
        ),
        migrations.AlterModelOptions(
            name='formacao',
            options={'permissions': (('formacao_list', 'Pode listar formação'), ('formacao_create', 'Pode cadastrar formação'), ('formacao_update', 'Pode editar formação'), ('formacao_view', 'Pode ver formação'), ('formacao_delete', 'Pode deletar formação'))},
        ),
        migrations.AlterModelOptions(
            name='municipio',
            options={'permissions': (('municipio_list', 'Pode listar município'), ('municipio_create', 'Pode cadastrar município'), ('municipio_update', 'Pode editar município'), ('municipio_view', 'Pode ver município'), ('municipio_delete', 'Pode deletar município'))},
        ),
        migrations.AlterModelOptions(
            name='natureza',
            options={'permissions': (('natureza_list', 'Pode listar natureza'), ('natureza_create', 'Pode cadastrar natureza'), ('natureza_update', 'Pode editar natureza'), ('natureza_view', 'Pode ver natureza'), ('natureza_delete', 'Pode deletar natureza'))},
        ),
        migrations.AlterModelOptions(
            name='subatividade',
            options={'permissions': (('subatividade_list', 'Pode listar subatividade'), ('subatividade_create', 'Pode cadastrar subatividade'), ('subatividade_update', 'Pode editar subatividade'), ('subatividade_view', 'Pode ver subatividade'), ('subatividade_delete', 'Pode deletar subatividade'))},
        ),
    ]