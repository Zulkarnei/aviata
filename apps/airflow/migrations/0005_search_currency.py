# Generated by Django 4.1.7 on 2023-02-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airflow', '0004_alter_search_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='currency',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Валюта'),
        ),
    ]
