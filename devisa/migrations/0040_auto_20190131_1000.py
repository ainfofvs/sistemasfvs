# Generated by Django 2.1.4 on 2019-01-31 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0039_entidadeunidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='entidadesubatividade',
            name='terceirizado',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, related_name='terceirizado', to='devisa.Entidade'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devisa.Area'),
        ),
        migrations.AlterField(
            model_name='bairro',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devisa.Municipio'),
        ),
        migrations.AlterField(
            model_name='entidaderesponsavel',
            name='entidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entidade', to='devisa.Entidade'),
        ),
        migrations.AlterField(
            model_name='entidaderesponsavel',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responsavel', to='devisa.Entidade'),
        ),
        migrations.AlterField(
            model_name='entidadesubatividade',
            name='entidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devisa.Entidade'),
        ),
        migrations.AlterField(
            model_name='entidadesubatividade',
            name='responsavel_tecnico',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='responsavel_tecnico', to='devisa.Entidade'),
        ),
        migrations.AlterField(
            model_name='entidadesubatividade',
            name='subatividade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subatividade', to='devisa.Subatividade'),
        ),
        migrations.AlterField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devisa.Pais'),
        ),
        migrations.AlterField(
            model_name='formacao',
            name='escolaridade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devisa.Escolaridade'),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devisa.Estado'),
        ),
        migrations.AlterField(
            model_name='subatividade',
            name='atividade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devisa.Atividade'),
        ),
    ]
