# Generated by Django 3.1 on 2020-08-15 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReservePrice',
            new_name='Price',
        ),
    ]
