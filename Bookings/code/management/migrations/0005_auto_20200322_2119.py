# Generated by Django 3.0.4 on 2020-03-22 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20200322_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(max_length=15),
        ),
    ]
