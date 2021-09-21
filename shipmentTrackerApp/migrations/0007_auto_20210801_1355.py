# Generated by Django 3.2.3 on 2021-08-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipmentTrackerApp', '0006_alter_ship_last_day_pricing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='date_booked',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='eta_disport',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='eta_gh',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='etd_gh',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='ship_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ship',
            name='ship_start',
            field=models.DateField(blank=True, null=True),
        ),
    ]