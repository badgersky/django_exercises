# Generated by Django 4.1.7 on 2023-02-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises_app', '0008_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='exercises_app.category'),
        ),
    ]
