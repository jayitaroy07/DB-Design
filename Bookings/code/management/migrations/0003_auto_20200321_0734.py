# Generated by Django 3.0.4 on 2020-03-21 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20200320_2122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'get_latest_by': 'address_id'},
        ),
        migrations.AlterModelOptions(
            name='phone',
            options={'get_latest_by': 'phone_id'},
        ),
    ]