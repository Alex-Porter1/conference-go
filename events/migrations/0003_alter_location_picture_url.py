# Generated by Django 4.0.6 on 2022-07-08 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_location_picture_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='picture_url',
            field=models.CharField(default='Null', max_length=255),
            preserve_default=False,
        ),
    ]
