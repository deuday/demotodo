# Generated by Django 3.2.16 on 2023-01-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tdapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2023-01-24'),
            preserve_default=False,
        ),
    ]
