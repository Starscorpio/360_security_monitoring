# Generated by Django 3.1.6 on 2021-07-01 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securecheck', '0024_auto_20210701_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thekeys',
            name='new_ID',
        ),
    ]
