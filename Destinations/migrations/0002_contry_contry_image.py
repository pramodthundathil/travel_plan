# Generated by Django 3.2.14 on 2024-01-09 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Destinations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contry',
            name='contry_image',
            field=models.FileField(default=1, upload_to='Contry_image'),
            preserve_default=False,
        ),
    ]
