# Generated by Django 4.1.7 on 2023-02-16 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airflow', '0002_alter_search_search_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='uid',
            new_name='uuid',
        ),
    ]