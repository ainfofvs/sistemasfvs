# Generated by Django 2.1.4 on 2019-01-28 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0036_auto_20190128_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidadesubatividade',
            name='responsavel',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsavel_tecnico', to='devisa.Entidade'),
        ),
    ]