# Generated by Django 2.1.4 on 2019-02-11 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0042_auto_20190208_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntidadeFormaproducao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devisa.Entidade')),
                ('forma_producao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='forma_producao', to='devisa.Formaproducao')),
            ],
        ),
    ]
