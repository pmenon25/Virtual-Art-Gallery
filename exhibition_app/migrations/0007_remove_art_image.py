# Generated by Django 3.2.8 on 2021-10-27 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition_app', '0006_delete_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='image',
        ),
    ]
