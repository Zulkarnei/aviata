# Generated by Django 4.1.7 on 2023-02-17 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_price_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='booking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='booking.booking'),
        ),
    ]
