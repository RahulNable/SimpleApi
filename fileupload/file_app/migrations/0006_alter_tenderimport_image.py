# Generated by Django 3.2.16 on 2022-11-30 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0005_auto_20221129_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenderimport',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
