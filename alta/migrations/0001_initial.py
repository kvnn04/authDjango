# Generated by Django 5.1.4 on 2025-01-11 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('apellido', models.CharField(max_length=70)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.CharField(max_length=150, unique=True)),
                ('pwd', models.CharField(max_length=70)),
            ],
        ),
    ]
