# Generated by Django 2.2.13 on 2020-07-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todolist_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='todolist',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]