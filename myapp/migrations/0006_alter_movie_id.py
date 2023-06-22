# Generated by Django 4.1.7 on 2023-04-08 17:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_movie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]