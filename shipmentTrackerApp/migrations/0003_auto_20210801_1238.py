# Generated by Django 3.2.3 on 2021-08-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipmentTrackerApp', '0002_alter_ship_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='date_booked',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='eta_disport',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='eta_gh',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='etd_gh',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='last_day_pricing',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='ship_end',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='ship_start',
            field=models.DateTimeField(blank=True),
        ),
    ]