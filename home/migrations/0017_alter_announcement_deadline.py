# Generated by Django 5.1.2 on 2024-11-21 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_announcement_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 11, 17, 25, 5, 147081, tzinfo=datetime.timezone.utc)),
        ),
    ]
