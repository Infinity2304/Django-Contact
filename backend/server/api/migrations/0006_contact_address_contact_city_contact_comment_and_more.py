# Generated by Django 5.1.7 on 2025-03-16 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='comment',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='pin',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.IntegerField(max_length=10, unique=True),
        ),
    ]
