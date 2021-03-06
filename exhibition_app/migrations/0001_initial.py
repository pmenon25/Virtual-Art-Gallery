# Generated by Django 3.2.8 on 2021-10-29 02:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('artist_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('likes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=80)),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('exhibition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibition_app.exhibition')),
            ],
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('exhibition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibition_app.exhibition')),
            ],
        ),
    ]
