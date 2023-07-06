# Generated by Django 4.2.3 on 2023-07-06 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='hybrid',
            new_name='hybrid_link',
        ),
        migrations.AddField(
            model_name='club',
            name='meeting_type',
            field=models.CharField(default='On Campus', max_length=100),
        ),
    ]
