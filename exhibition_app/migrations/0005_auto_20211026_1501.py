# Generated by Django 3.2.8 on 2021-10-26 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition_app', '0004_exhibition_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('exhibition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibition_app.exhibition')),
            ],
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
