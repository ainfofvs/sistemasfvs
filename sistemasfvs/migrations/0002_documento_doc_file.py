# Generated by Django 2.1.4 on 2018-12-20 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemasfvs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='doc_file',
            field=models.FileField(blank=True, null=True, upload_to='doctos_files'),
        ),
    ]
