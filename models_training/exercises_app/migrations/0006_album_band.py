# Generated by Django 4.1.7 on 2023-02-22 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises_app', '0005_alter_album_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exercises_app.band'),
        ),
    ]
