# Generated by Django 4.1.7 on 2023-04-08 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_movie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='t_rating',
            field=models.IntegerField(default=1000),
        ),
    ]
