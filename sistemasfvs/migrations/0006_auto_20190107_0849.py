# Generated by Django 2.1.4 on 2019-01-07 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemasfvs', '0005_auto_20181227_0852'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documento',
            options={'permissions': (('documento_list', 'Pode listar documento'), ('documento_create', 'Pode cadastrar documento'), ('documento_update', 'Pode editar documento'), ('documento_view', 'Pode ver documento'), ('documento_delete', 'Pode deletar documento'))},
        ),
        migrations.AlterModelOptions(
            name='fase',
            options={'permissions': (('fase_list', 'Pode listar fase'), ('fase_create', 'Pode cadastrar fase'), ('fase_add', 'Pode alterar fase de projeto'), ('fase_sf_delete', 'Pode excluir fase de projeto'), ('fase_sf_update', 'Pode alterar fase de projeto'), ('fase_update', 'Pode editar fase'), ('fase_view', 'Pode ver fase'), ('fase_delete', 'Pode deletar fase'))},
        ),
        migrations.AlterModelOptions(
            name='sistema',
            options={'permissions': (('sistema_list', 'Pode listar projeto'), ('sistema_create', 'Pode cadastrar projeto'), ('sistema_update', 'Pode editar projeto'), ('sistema_view', 'Pode ver projeto'), ('sistema_delete', 'Pode deletar projeto'), ('sistema_doctos', 'Pode ver documentos do projeto'), ('sistema_fases', 'Pode ver fases do projeto'))},
        ),
        migrations.AlterModelOptions(
            name='sistemafase',
            options={'permissions': (('sistemafase_list', 'Pode listar sistemafase'), ('sistemafase_create', 'Pode cadastrar sistemafase'), ('sistemafase_update', 'Pode editar sistemafase'), ('sistemafase_view', 'Pode ver sistemafase'), ('sistemafase_delete', 'Pode deletar sistemafase'))},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'permissions': (('status_list', 'Pode listar status'), ('status_create', 'Pode cadastrar status'), ('status_update', 'Pode editar status'), ('status_view', 'Pode ver status'), ('status_delete', 'Pode deletar status'))},
        ),
    ]
