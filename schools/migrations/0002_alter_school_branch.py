# Generated by Django 4.1.7 on 2023-02-23 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='branch',
            field=models.IntegerField(max_length=5, unique=True),
        ),
    ]