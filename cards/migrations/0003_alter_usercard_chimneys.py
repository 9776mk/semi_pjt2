# Generated by Django 3.2.13 on 2022-11-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_alter_usercard_chimneys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercard',
            name='chimneys',
            field=models.IntegerField(blank=True),
        ),
    ]
