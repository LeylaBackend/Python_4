# Generated by Django 4.2.8 on 2023-12-21 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_categories_type_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories_type',
            old_name='text',
            new_name='title',
        ),
    ]