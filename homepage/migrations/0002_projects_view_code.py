# Generated by Django 4.0.6 on 2022-08-26 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='view_code',
            field=models.BooleanField(default=False),
        ),
    ]