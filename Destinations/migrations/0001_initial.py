# Generated by Django 3.2.14 on 2024-01-09 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_name', models.CharField(max_length=255)),
                ('key_words', models.CharField(max_length=255)),
                ('image', models.FileField(upload_to='destination_image')),
                ('place', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('attractions', models.CharField(max_length=1000)),
                ('address', models.TextField(max_length=1000)),
                ('postel_code', models.IntegerField()),
                ('contry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Destinations.contry')),
            ],
        ),
    ]