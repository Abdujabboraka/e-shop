# Generated by Django 5.1.1 on 2024-10-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_announcement_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
