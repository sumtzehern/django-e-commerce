# Generated by Django 5.0.6 on 2024-06-28 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_category_options_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='create_by',
            new_name='created_by',
        ),
    ]
