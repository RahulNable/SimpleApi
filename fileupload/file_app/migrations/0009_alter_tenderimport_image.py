# Generated by Django 3.2.16 on 2022-12-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0008_alter_tenderimport_customerrefno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenderimport',
            name='Image',
            field=models.BinaryField(blank=True, max_length='max', null=True),
        ),
    ]
