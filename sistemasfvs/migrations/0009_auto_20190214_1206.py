# Generated by Django 2.1.4 on 2019-02-14 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemasfvs', '0008_auto_20190211_1106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sistema',
            options={'permissions': (('sistema_list', 'Pode listar projeto'), ('sistema_create', 'Pode cadastrar projeto'), ('sistema_update', 'Pode editar projeto'), ('sistema_view', 'Pode ver projeto'), ('sistema_delete', 'Pode deletar projeto'), ('sistema_doctos', 'Pode ver documentos do projeto'), ('sistema_fases', 'Pode ver fases do projeto'), ('perfil', 'Pode acessar o perfil do usuario'))},
        ),
    ]
