# Generated by Django 3.1.6 on 2021-06-29 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securecheck', '0018_form_location_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freq',
            name='freq_data',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='freq',
            name='freq_msg',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='notifi',
            name='actual_data',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='notifi',
            name='message_display',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
