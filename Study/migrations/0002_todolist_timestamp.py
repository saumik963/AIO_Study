# Generated by Django 4.2.3 on 2023-09-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default='2023-09-24'),
            preserve_default=False,
        ),
    ]
