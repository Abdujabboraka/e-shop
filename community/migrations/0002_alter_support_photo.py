# Generated by Django 5.1.2 on 2024-11-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='support/'),
        ),
    ]