# Generated by Django 3.1.7 on 2021-05-16 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cantor', '0002_remove_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]
