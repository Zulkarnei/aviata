# Generated by Django 4.1.7 on 2023-02-17 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_alter_price_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='booking',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.booking'),
        ),
    ]
