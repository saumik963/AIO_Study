# Generated by Django 4.2.3 on 2024-02-08 12:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0007_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
