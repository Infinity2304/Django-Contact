# Generated by Django 5.1.7 on 2025-03-15 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='hashed_password',
            new_name='password',
        ),
    ]
