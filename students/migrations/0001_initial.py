# Generated by Django 4.1.7 on 2023-03-11 16:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75, unique=True)),
                ('date_of_birth', models.CharField(max_length=10)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('phone', models.CharField(max_length=14)),
                ('gender', models.CharField(choices=[('masculino', 'Masculine'), ('feminino', 'Feminine'), ('lgbt', 'Lgbt'), ('outro', 'Other')], default='outro', max_length=20)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='schools.school')),
            ],
        ),
    ]
