# Generated by Django 3.1.2 on 2022-09-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_remove_phone_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]