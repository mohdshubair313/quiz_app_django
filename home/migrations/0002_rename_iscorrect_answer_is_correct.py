# Generated by Django 5.1.4 on 2024-12-18 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='iscorrect',
            new_name='is_correct',
        ),
    ]
