# Generated by Django 2.1.7 on 2019-03-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innotech', '0006_auto_20190321_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='summary',
            field=models.TextField(max_length=50),
        ),
    ]
