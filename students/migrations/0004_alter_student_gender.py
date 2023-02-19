# Generated by Django 4.1.7 on 2023-02-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('masculino', 'Masculine'), ('feminino', 'Feminine'), ('lgbtqia+', 'Lgbt'), ('outro', 'Other')], default='outro', max_length=20),
        ),
    ]