# Generated by Django 4.1.7 on 2023-02-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_flight_booking_alter_flight_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segment',
            name='equipment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
