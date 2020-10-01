# Generated by Django 3.1.1 on 2020-10-01 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('iata', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('lat', models.DecimalField(decimal_places=16, max_digits=22)),
                ('lon', models.DecimalField(decimal_places=16, max_digits=22)),
            ],
        ),
    ]