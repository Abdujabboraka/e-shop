# Generated by Django 5.1.2 on 2024-11-22 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_announcement_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 12, 17, 44, 14, 714477, tzinfo=datetime.timezone.utc)),
        ),
    ]
