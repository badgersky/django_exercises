# Generated by Django 4.1.7 on 2023-03-02 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director', to='manage_movies.person')),
                ('screenplay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenplay', to='manage_movies.person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=128, null=True)),
                ('year', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('genre', models.ManyToManyField(to='manage_movies.genre')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_movies.movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_movies.person')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='starring',
            field=models.ManyToManyField(through='manage_movies.PersonMovie', to='manage_movies.person'),
        ),
    ]
