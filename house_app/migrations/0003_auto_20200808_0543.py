# Generated by Django 3.0.8 on 2020-08-08 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_app', '0002_auto_20200807_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='image1',
            field=models.ImageField(default='default.jpg', upload_to='houses'),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='image1',
            field=models.ImageField(default='default.jpg', upload_to='houses'),
        ),
    ]
