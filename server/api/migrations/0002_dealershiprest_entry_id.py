# Generated by Django 3.2.10 on 2021-12-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealershiprest',
            name='entry_id',
            field=models.IntegerField(default=999, unique=True),
        ),
    ]
