# Generated by Django 4.1.7 on 2023-03-03 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NFTMile', '0002_alter_data_lat_alter_data_lon'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Data',
        ),
    ]