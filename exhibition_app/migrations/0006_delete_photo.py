# Generated by Django 3.2.8 on 2021-10-27 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition_app', '0005_alter_art_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
    ]