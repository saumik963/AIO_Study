# Generated by Django 4.2.3 on 2024-02-08 12:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0009_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
