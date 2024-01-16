# Generated by Django 3.2.14 on 2024-01-16 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Destinations', '0008_hotels_restaurants_tourguids'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='Time_Taken_toTravel_in_Hours',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotels',
            name='Room_Category',
            field=models.CharField(choices=[('single', 'single'), ('double', 'double'), ('suite', 'suite'), ('dormetory', 'dormetory')], max_length=255),
        ),
    ]