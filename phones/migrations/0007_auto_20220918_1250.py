# Generated by Django 3.1.2 on 2022-09-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_phone_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='phones/images/'),
        ),
    ]