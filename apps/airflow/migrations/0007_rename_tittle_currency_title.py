# Generated by Django 4.1.7 on 2023-02-17 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airflow', '0006_currency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency',
            old_name='tittle',
            new_name='title',
        ),
    ]