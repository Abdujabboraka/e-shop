# Generated by Django 5.1.2 on 2024-11-22 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_announcement_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 12, 9, 13, 21, 403272, tzinfo=datetime.timezone.utc)),
        ),
    ]
