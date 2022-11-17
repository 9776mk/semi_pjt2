# Generated by Django 3.2.13 on 2022-11-16 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('is_private', models.BooleanField()),
                ('socks', models.IntegerField()),
                ('chimneys', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('socks', models.IntegerField(blank=True)),
                ('chimneys', models.IntegerField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ribbons', models.IntegerField()),
                ('id_text', models.TextField(blank=True)),
                ('read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('usercard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.usercard')),
            ],
        ),
        migrations.CreateModel(
            name='Groupcomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ribbons', models.IntegerField()),
                ('id_text', models.TextField(blank=True)),
                ('groupcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.groupcard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupcard_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
