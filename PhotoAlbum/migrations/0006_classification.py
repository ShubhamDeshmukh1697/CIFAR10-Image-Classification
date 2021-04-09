# Generated by Django 3.1.7 on 2021-04-05 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoAlbum', '0005_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='results/')),
                ('classification_category', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
