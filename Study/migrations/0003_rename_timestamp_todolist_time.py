# Generated by Django 4.2.3 on 2023-09-24 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0002_todolist_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='timestamp',
            new_name='time',
        ),
    ]
