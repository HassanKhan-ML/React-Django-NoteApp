# Generated by Django 4.0.1 on 2022-01-20 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_note_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='user',
        ),
    ]