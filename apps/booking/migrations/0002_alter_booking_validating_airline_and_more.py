# Generated by Django 4.1.7 on 2023-02-16 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='validating_airline',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='segment',
            name='baggage',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='segment',
            name='marketing_airline',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='segment',
            name='operating_airline',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
