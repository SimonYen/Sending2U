# Generated by Django 4.1 on 2022-09-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0003_file_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='raw_data',
            field=models.FileField(upload_to='files'),
        ),
    ]