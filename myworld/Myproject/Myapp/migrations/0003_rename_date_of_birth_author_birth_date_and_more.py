# Generated by Django 4.2.4 on 2024-03-08 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_author_editor_reader_remove_album_artist_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='date_of_birth',
            new_name='birth_date',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 8, 11, 53, 6, 223381, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='author',
            name='title',
            field=models.CharField(default='Mr', max_length=3),
        ),
    ]