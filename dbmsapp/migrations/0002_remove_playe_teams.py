# Generated by Django 2.2.2 on 2020-04-10 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbmsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playe',
            name='teams',
        ),
    ]