# Generated by Django 3.1.7 on 2021-04-08 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoAlbum', '0008_remove_image_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification',
            name='label',
            field=models.CharField(default='AEROPLANE', max_length=50),
        ),
    ]
