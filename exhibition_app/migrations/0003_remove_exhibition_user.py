# Generated by Django 3.2.8 on 2021-10-23 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition_app', '0002_exhibition_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibition',
            name='user',
        ),
    ]