# Generated by Django 4.1.7 on 2023-02-18 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='date_joined',
            new_name='created_at',
        ),
    ]
