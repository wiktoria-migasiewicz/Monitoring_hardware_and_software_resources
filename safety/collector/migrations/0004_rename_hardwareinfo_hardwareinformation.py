# Generated by Django 5.0 on 2024-01-03 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0003_hardwareinfo_softwareinformation_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HardwareInfo',
            new_name='HardwareInformation',
        ),
    ]
