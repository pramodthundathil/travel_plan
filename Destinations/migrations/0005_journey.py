# Generated by Django 3.2.14 on 2024-01-12 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Destinations', '0004_auto_20240109_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staring_from', models.CharField(max_length=255)),
                ('straing_time', models.TimeField()),
                ('destination', models.CharField(max_length=255)),
                ('ending_time', models.TimeField()),
                ('mode_of_travel', models.CharField(choices=[('air', 'air'), ('train', 'train'), ('bus', 'bus'), ('other', 'other')], max_length=255)),
                ('cost', models.IntegerField()),
                ('total_Kilomeaters', models.FloatField()),
                ('destination_include', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Destinations.destination')),
            ],
        ),
    ]