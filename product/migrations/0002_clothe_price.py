# Generated by Django 4.2.8 on 2023-12-28 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothe',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
