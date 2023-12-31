# Generated by Django 4.2.3 on 2023-07-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_customuser_clubs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Mentee Email')),
                ('first_name', models.CharField(max_length=100, verbose_name='Mentee First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Mentee Last Name')),
                ('emplid', models.IntegerField(default=0, verbose_name='EmplID')),
                ('major', models.CharField(max_length=100, verbose_name='Mentee Major')),
                ('preferred_language', models.CharField(max_length=100, verbose_name='Prefferred Language')),
            ],
        ),
    ]
