# Generated by Django 5.0.2 on 2024-02-26 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getInfo', '0003_alter_station_category_id_alter_station_id_state_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GetDataSynop_main',
            new_name='GetDataSynop',
        ),
    ]
