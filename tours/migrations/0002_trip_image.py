# Generated by Django 5.0.2 on 2024-03-02 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='image',
            field=models.ImageField(default='france.jpg', upload_to='trip_images/'),
            preserve_default=False,
        ),
    ]
