# Generated by Django 3.2.10 on 2021-12-17 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_reviewrest_dealership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrest',
            name='id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
    ]
