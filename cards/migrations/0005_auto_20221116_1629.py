# Generated by Django 3.2.13 on 2022-11-16 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20221115_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercomment',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]