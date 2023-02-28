# Generated by Django 4.1.7 on 2023-02-23 20:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('zip_code', models.CharField(max_length=8)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]
