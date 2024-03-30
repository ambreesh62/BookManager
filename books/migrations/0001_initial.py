# Generated by Django 5.0.3 on 2024-03-27 22:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('nationaly', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titel', models.CharField(max_length=150)),
                ('genre', models.CharField(max_length=150)),
                ('published_Date', models.DateField()),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]