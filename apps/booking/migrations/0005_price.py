# Generated by Django 4.1.7 on 2023-02-17 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_segment_equipment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(blank=True, null=True)),
                ('base', models.FloatField(blank=True, null=True)),
                ('taxes', models.FloatField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
            ],
        ),
    ]