# Generated by Django 2.2.2 on 2020-04-10 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbmsapp', '0004_remove_playe_teams'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tea',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='playe',
            name='team_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='dbmsapp.tea', verbose_name='Category'),
        ),
    ]
