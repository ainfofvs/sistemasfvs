# Generated by Django 2.1.4 on 2019-02-11 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0043_entidadeformaproducao'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntidadeClasseproducao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe_producao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='classe_producao', to='devisa.Classeproducao')),
                ('entidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devisa.Entidade')),
            ],
        ),
    ]
