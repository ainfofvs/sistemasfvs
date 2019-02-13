# Generated by Django 2.1.4 on 2019-01-21 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0031_entidadesubatividade'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntidadeResponsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entidade', to='devisa.Entidade')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsavel', to='devisa.Entidade')),
            ],
            options={
                'permissions': (('entresp_list', 'Pode listar responsável legal do estabelecimento'), ('entresp_create', 'Pode incluir responsável legal do estabelecimento'), ('entresp_delete', 'Pode deletar responsável legal do estabelecimento')),
            },
        ),
    ]