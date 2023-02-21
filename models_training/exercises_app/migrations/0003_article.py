# Generated by Django 4.1.7 on 2023-02-21 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises_app', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=64, null=True)),
                ('content', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Still Writing'), (1, 'Awaits Review'), (2, 'Published')], default=0)),
                ('start_date', models.DateField(null=True)),
                ('stop_date', models.DateField(null=True)),
            ],
        ),
    ]
