# Generated by Django 3.1 on 2020-08-16 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0003_auto_20200816_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='field',
            old_name='field_type_id',
            new_name='field_type',
        ),
        migrations.RenameField(
            model_name='price',
            old_name='field_id',
            new_name='field',
        ),
    ]
