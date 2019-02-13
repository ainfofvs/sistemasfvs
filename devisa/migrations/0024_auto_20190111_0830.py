# Generated by Django 2.1.4 on 2019-01-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0023_auto_20190111_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidade',
            name='ent_cnpj',
            field=models.CharField(default=1, max_length=30, verbose_name='CNPJ'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_nome_razao',
            field=models.CharField(max_length=300, verbose_name='nome / Razão Social'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='ent_tipo_entidade',
            field=models.CharField(max_length=2, verbose_name='tipo de entidade'),
        ),
    ]
