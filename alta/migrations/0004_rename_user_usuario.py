# Generated by Django 5.1.4 on 2025-01-13 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alta', '0003_rename_usuario_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Usuario',
        ),
    ]
