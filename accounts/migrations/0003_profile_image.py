# Generated by Django 5.0.6 on 2024-08-08 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_country_profile_delete_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='', upload_to='profile/'),
            preserve_default=False,
        ),
    ]