# Generated by Django 2.1.7 on 2019-03-26 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innotech', '0007_auto_20190321_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
