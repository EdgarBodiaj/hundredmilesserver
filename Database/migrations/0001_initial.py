# Generated by Django 4.1.7 on 2023-03-03 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=200)),
                ('group', models.IntegerField()),
                ('lat', models.DecimalField(decimal_places=16, max_digits=200)),
                ('lon', models.DecimalField(decimal_places=16, max_digits=200)),
                ('color', models.CharField(max_length=200)),
                ('ang', models.DecimalField(decimal_places=16, max_digits=200)),
                ('radius', models.IntegerField()),
            ],
        ),
    ]
