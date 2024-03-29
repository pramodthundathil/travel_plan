# Generated by Django 3.2.14 on 2024-01-18 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Destinations', '0013_auto_20240118_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='Time_Taken_toTravel_in_Hours',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='journey',
            name='cost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='journey',
            name='destination',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='journey',
            name='ending_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='journey',
            name='mode_of_travel',
            field=models.CharField(blank=True, choices=[('air', 'air'), ('train', 'train'), ('bus', 'bus'), ('other', 'other')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='journey',
            name='staring_from',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='journey',
            name='straing_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='journey',
            name='total_Kilomeaters',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
