# Generated by Django 2.2.19 on 2023-10-10 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20231010_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='group_menu',
        ),
        migrations.DeleteModel(
            name='GroupMenu',
        ),
    ]
