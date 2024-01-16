# Generated by Django 3.2.14 on 2024-01-15 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Destinations', '0006_auto_20240112_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='destination_include',
        ),
        migrations.AddField(
            model_name='journey',
            name='destination_include',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Destinations.destination'),
        ),
    ]