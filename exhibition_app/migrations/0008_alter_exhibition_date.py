# Generated by Django 3.2.8 on 2021-10-25 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition_app', '0007_alter_exhibition_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]