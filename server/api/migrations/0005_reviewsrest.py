# Generated by Django 3.2.10 on 2021-12-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211217_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewsRest',
            fields=[
                ('_id', models.CharField(default='default_id', max_length=100)),
                ('_rev', models.CharField(blank=True, max_length=100, null=True)),
                ('id', models.CharField(blank=True, max_length=100, primary_key=True, serialize=False)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('st', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=100, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('short_name', models.CharField(blank=True, max_length=100, null=True)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
