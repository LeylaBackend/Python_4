# Generated by Django 4.2.8 on 2023-12-21 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_categories_type_alter_category_product_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categorie',
        ),
    ]
