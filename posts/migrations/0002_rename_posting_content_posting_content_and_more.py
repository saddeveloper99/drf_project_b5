# Generated by Django 4.2.1 on 2023-05-08 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posting',
            old_name='posting_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='posting',
            old_name='posting_image',
            new_name='image',
        ),
    ]
