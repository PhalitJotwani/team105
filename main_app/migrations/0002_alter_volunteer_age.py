# Generated by Django 4.0.5 on 2022-06-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='age',
            field=models.IntegerField(),
        ),
    ]
