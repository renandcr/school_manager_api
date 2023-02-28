# Generated by Django 4.1.7 on 2023-02-23 20:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('branch', models.IntegerField(max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75, unique=True)),
                ('zip_code', models.CharField(max_length=8)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=14)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
