# Generated by Django 5.1.2 on 2024-11-22 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_alter_support_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='opinion',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
