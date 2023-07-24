# Generated by Django 4.2.1 on 2023-07-19 06:36

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
            name='signUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=10, null=True)),
                ('branch', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=15)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadDate', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('NotesFile', models.FileField(upload_to='')),
                ('FileType', models.CharField(max_length=30)),
                ('Decription', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]